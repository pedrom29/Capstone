from django.shortcuts import redirect, render, get_object_or_404
from .models import Product, Cart, CartItem, Order, OrderItem
from django.contrib.sessions.models import Session
from .forms import OrderForm
from datetime import date, timedelta
from .models import Order
from django.shortcuts import redirect
from transbank.webpay.webpay_plus.transaction import Transaction, WebpayOptions
from transbank.common.integration_type import IntegrationType
from django.conf import settings 
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.core.mail import send_mail
from django.http import JsonResponse
import random
from random import shuffle


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Manejar carritos de usuarios autenticados
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user)
    else:
        # Manejar carritos de usuarios invitados
        session_id = request.session.session_key
        if not session_id:
            request.session.create()
            session_id = request.session.session_key
        carts = Cart.objects.filter(session_id=session_id)

    # Si hay más de un carrito, usar el más reciente y eliminar duplicados
    if carts.exists():
        cart = carts.latest('created_at')  # Elige el más reciente
        # Elimina duplicados si hay más de un carrito
        carts.exclude(id=cart.id).delete()
    else:
        cart = Cart.objects.create(
            user=request.user if request.user.is_authenticated else None,
            session_id=request.session.session_key
        )

    # Agregar producto al carrito
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect('cart_detail')


def cart_detail(request):
    if not request.session.session_key:
        request.session.create()
    session_id = request.session.session_key

    # Obtener el carrito
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        cart, created = Cart.objects.get_or_create(session_id=session_id)

    cart_items = cart.cartitem_set.all()
    total = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'store/cart_detail.html', {
        'cart_items': cart_items,
        'total': total,
    })

def update_cart_item(request, item_id, action):
    cart_item = get_object_or_404(CartItem, id=item_id)
    
    if action == 'increment':
        cart_item.quantity += 1
    elif action == 'decrement':
        cart_item.quantity -= 1
        if cart_item.quantity <= 0:
            cart_item.delete()  # Eliminar si la cantidad llega a 0
            return redirect('cart_detail')
    elif action == 'delete':
        cart_item.delete()  # Eliminar directamente el ítem
        return redirect('cart_detail')
    
    cart_item.save()
    return redirect('cart_detail')

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart_detail')

def product_list(request):
    # Consulta todos los productos
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

def checkout(request):
    # Manejar el carrito basado en el tipo de usuario
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
    else:
        session_id = request.session.session_key
        if not session_id:  # Crear una nueva sesión si no existe
            request.session.create()
            session_id = request.session.session_key
        cart = Cart.objects.filter(session_id=session_id).first()

    # Verificar si el carrito existe y tiene ítems
    if not cart:
        return redirect('cart_detail')  # Redirigir si no hay carrito

    cart_items = cart.cartitem_set.all()
    if not cart_items:
        return redirect('cart_detail')  # Redirigir si el carrito está vacío

    total = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Crear el pedido
            order = Order.objects.create(
                user=request.user if request.user.is_authenticated else None,
                address=form.cleaned_data['address'],
                comuna=form.cleaned_data['comuna'],
                city=form.cleaned_data['city'],
                phone=form.cleaned_data['phone'],
                delivery_date=form.cleaned_data['delivery_date'],
                total=total,
            )

            # Crear los ítems del pedido
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity
                )

            # Vaciar el carrito
            cart_items.delete()
            return redirect('payment', order_id=order.id)

    else:
        form = OrderForm()

    return render(request, 'store/checkout.html', {
        'form': form,
        'cart_items': cart_items,
        'total': total,
    })

def payment(request, order_id):
    # Buscar el pedido según el tipo de usuario
    if request.user.is_authenticated:
        order = get_object_or_404(Order, id=order_id, user=request.user)
    else:
        # Usuarios invitados: el pedido debe tener un usuario `null`
        order = get_object_or_404(Order, id=order_id, user__isnull=True)

    return render(request, 'store/payment.html', {
        'order': order,
    })

def webpay_initiate(request, order_id):
    # Buscar el pedido según el tipo de usuario
    if request.user.is_authenticated:
        order = get_object_or_404(Order, id=order_id, user=request.user)
        session_id = str(request.user.id)  # Para usuarios autenticados, usar el ID del usuario
    else:
        order = get_object_or_404(Order, id=order_id, user__isnull=True)
        session_id = request.session.session_key  # Para invitados, usar el session_id

    # Configuración de la transacción
    tx = Transaction(WebpayOptions(
        commerce_code=settings.WEBPAY_COMMERCE_CODE,
        api_key=settings.WEBPAY_API_KEY,
        integration_type=IntegrationType.TEST
    ))

    # Crear la transacción con Webpay
    response = tx.create(
        buy_order=str(order.id),  # Tu referencia interna
        session_id=str(request.session.session_key or request.user.id),
        amount=order.total,
        return_url=settings.WEBPAY_RETURN_URL
    )

    # Redirigir al formulario de pago de Webpay
    return redirect(response['url'] + '?token_ws=' + response['token'])

def webpay_response(request):
    token = request.GET.get('token_ws')
    if not token:
        return render(request, 'store/payment_failed.html')

    tx = Transaction(WebpayOptions(
        commerce_code=settings.WEBPAY_COMMERCE_CODE,
        api_key=settings.WEBPAY_API_KEY,
        integration_type=IntegrationType.TEST
    ))

    # Procesar el token y obtener la respuesta
    response = tx.commit(token=token)

    if response['status'] == 'AUTHORIZED':
        order = Order.objects.get(id=response['buy_order'])
        order.paid = True
        order.save()

        # Pasar datos relevantes al template
        return render(request, 'store/payment_success.html', {
            'authorization_code': response.get('authorization_code'),
            'buy_order': response.get('buy_order'),
            'transaction_date': response.get('transaction_date'),
            'amount': response.get('amount'),
        })
    else:
        return render(request, 'store/payment_failed.html', {
            'response': response
        })
    
#Email de confirmación
def send_confirmation_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        buy_order = request.POST.get('buy_order')

        # Obtener los detalles del pedido
        order = get_object_or_404(Order, id=buy_order)
        subject = f"Confirmación de Compra - Pedido {order.id}"
        message = f"""
        ¡Gracias por tu compra!
        
        Detalles del Pedido:
        - ID del Pedido: {order.id}
        - Fecha: {order.created_at}
        - Total: ${order.total}
        - Productos:
        """
        for item in order.items.all():
            message += f"\n  - {item.product.name} x {item.quantity} (${item.product.price * item.quantity})"

        message += f"\n\nGracias por comprar con nosotros."

        # Configurar el mensaje con codificación UTF-8
        email_message = EmailMessage(
            subject,
            message,
            to=[email]
        )
        email_message.encoding = 'utf-8'  # Especificar codificación
        email_message.send()

        return render(request, 'store/email_sent.html', {'email': email})

#Descargar comprobante PDF    
def download_invoice_pdf(request):
    if request.method == 'POST':
        buy_order = request.POST.get('buy_order')
        
        # Obtener el pedido
        order = Order.objects.get(id=buy_order)
        
        # Crear el PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="Factura_{order.id}.pdf"'

        # Crear el objeto canvas para generar el PDF
        p = canvas.Canvas(response)
        
        # Añadir contenido al PDF
        p.drawString(100, 800, "Factura de Compra")
        p.drawString(100, 780, f"ID del Pedido: {order.id}")
        p.drawString(100, 760, f"Fecha: {order.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        p.drawString(100, 740, f"Total: ${order.total}")
        p.drawString(100, 720, "Productos:")

        y = 700
        for item in order.items.all():
            p.drawString(120, y, f"{item.product.name} x {item.quantity} - ${item.product.price * item.quantity}")
            y -= 20

        # Finalizar el PDF
        p.showPage()
        p.save()

        return response
    
#def test_email(request):
#    send_mail(
#        'Prueba de Correo',  # Asunto
#        'Este es un correo de prueba enviado desde mi proyecto Django.',  # Cuerpo del mensaje
#        'tu_correo@gmail.com',  # Desde este correo (EMAIL_HOST_USER)
#        ['pe.maturana29@gmail.com'],  # A este correo
#        fail_silently=False,
#    )
#    return HttpResponse("Correo enviado exitosamente.")

def react_view(request):
    return render(request, 'react_index.html')

def product_list_json(request):
    products = Product.objects.all()
    products_data = [
        {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": float(product.price),
            "stock": product.stock,
            "image": product.image.url if product.image else None,
        }
        for product in products
    ]
    return JsonResponse({"products": products_data})

def payment_failed(request):
    # Simulación de datos de respuesta de error
    response_data = {
        'status': 'Transacción fallida',
        'detail': 'No se pudieron procesar los fondos, por favor intenta nuevamente.'
    }
    
    context = {
        'response': response_data
    }
    return render(request, 'store/payment_failed.html', context)

def base(request):
    return render(request, 'base.html')

def register_view(request):
    form = YourRegistrationForm() # type: ignore
    return render(request, 'register.html', {'form': form})

def home(request):
    products = list(Product.objects.annotate(count=Count('id')))  # Convierte el QuerySet en una lista
    shuffle(products)  # Mezcla los productos
    random_products = products[:4]  # Toma los primeros 4 después de mezclar
    return render(request, 'base.html', {'random_products': random_products})