from django.shortcuts import redirect, render, get_object_or_404
from .models import Product, Cart, CartItem, Order, OrderItem, Category
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
from random import sample 
from random import shuffle
from django.db.models import Count
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import os
from io import BytesIO
from decimal import Decimal
from .utils import generate_invoice_pdf
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from django.contrib import messages
from django.db import transaction


def login_view(request):
    # Lógica de inicio de sesión
    messages.success(request, "Has iniciado sesión correctamente.")
    return redirect("login")

def logout_view(request):
    # Lógica de cierre de sesión
    messages.success(request, "Has cerrado sesión correctamente.")
    return redirect("login")


def home(request):
    # Obtén todos los productos
    all_products = list(Product.objects.all())

    # Selecciona hasta 8 productos al azar
    featured_products = sample(all_products, min(len(all_products), 8))

    return render(request, 'store/home.html', {
        'featured_products': featured_products
    })

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

    # Método para formatear como precio en CLP
    def format_clp(value):
        return f"${value:,.0f}".replace(",", ".")

    formatted_total = format_clp(total)

    return render(request, 'store/cart_detail.html', {
        'cart_items': cart_items,
        'total': formatted_total,
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
    category_id = request.GET.get('category')  # Obtener la categoría seleccionada
    categories = Category.objects.all()  # Obtener todas las categorías

    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    return render(request, 'store/product_list.html', {
        'products': products,
        'categories': categories,
    })


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

    # Calcular el total y formatearlo
    total = sum(item.product.price * item.quantity for item in cart_items)
    formatted_total = f"${total:,.0f}".replace(",", ".")

    # Formatear los totales individuales de los ítems
    for item in cart_items:
        item.formatted_price = f"${item.product.price:,.0f}".replace(",", ".")
        item.formatted_total = f"${(item.product.price * item.quantity):,.0f}".replace(",", ".")

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
        'total': formatted_total,
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
    
def send_confirmation_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        buy_order = request.POST.get('buy_order')

        # Obtener los detalles del pedido
        order = get_object_or_404(Order, id=buy_order)

        # Generar el PDF
        pdf_buffer = generate_styled_invoice_pdf(order)

        # Configurar el correo
        subject = f"Confirmación de Compra - Pedido {order.id}"
        message = "Gracias por tu compra. Adjuntamos la factura de tu pedido."
        email_message = EmailMessage(
            subject,
            message,
            'tuemail@example.com',
            [email],
        )
        email_message.attach(f"Factura_{order.id}.pdf", pdf_buffer.read(), 'application/pdf')
        email_message.send()

        return render(request, 'store/email_sent.html', {'email': email})

# Descargar comprobante PDF con estilos
def download_invoice_pdf(request):
    if request.method == 'POST':
        buy_order = request.POST.get('buy_order')
        
        # Obtener el pedido
        order = Order.objects.get(id=buy_order)

        # Crear el PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="Factura_{order.id}.pdf"'

        # Configurar el documento
        doc = SimpleDocTemplate(response, pagesize=letter, rightMargin=50, leftMargin=50, topMargin=50, bottomMargin=50)
        styles = getSampleStyleSheet()

        # Contenido del PDF
        elements = []

        # Añadir el logo
        logo_path = os.path.join(settings.BASE_DIR, 'store/static/images/logo.png')  # Ruta absoluta al logo
        if os.path.exists(logo_path):
            logo = Image(logo_path, width=100, height=100)  # Ajusta el tamaño según sea necesario
            logo.hAlign = 'LEFT'
            elements.append(logo)

        # Título
        title = Paragraph("Factura de Compra", styles['Title'])
        elements.append(title)
        elements.append(Paragraph("<br/>", styles['Normal']))

        # Detalles del pedido
        order_details = [
            ["ID del Pedido:", f"{order.id}"],
            ["Fecha:", f"{order.created_at.strftime('%Y-%m-%d %H:%M:%S')}"],
            ["Total:", f"${order.total:,.0f}".replace(",", ".")],
        ]
        table = Table(order_details, hAlign='LEFT')
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
            ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        elements.append(table)
        elements.append(Paragraph("<br/><br/>", styles['Normal']))

        # Productos
        elements.append(Paragraph("<strong>Productos:</strong>", styles['Heading2']))
        product_data = [["Producto", "Cantidad", "Precio Unitario", "Total"]]
        for item in order.items.all():
            product_data.append([
                item.product.name,
                item.quantity,                
                f"${item.product.price:,.0f}".replace(",", "."),
                f"${item.product.price * item.quantity:,.0f}".replace(",", "."),
            ])

        product_table = Table(product_data, hAlign='LEFT', colWidths=[200, 100, 100, 100])
        product_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
            ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        elements.append(product_table)
        elements.append(Paragraph("<br/><br/>", styles['Normal']))

        # Nota al pie
        footer = Paragraph("&copy; 2024 Seifer - Jabones Reciclados. Gracias por tu compra.", styles['Normal'])
        elements.append(footer)

        # Construir el PDF
        doc.build(elements)

        return response

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


def generate_styled_invoice_pdf(order):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    # Estilo del documento
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    subtitle_style = styles['Heading2']
    normal_style = styles['Normal']

    # Encabezado
    logo_path = os.path.join(settings.BASE_DIR, 'store/static/images/logo.png')  # Ruta absoluta al logo
    if os.path.exists(logo_path):
        logo = Image(logo_path, width=100, height=100)  # Ajusta el tamaño según sea necesario
        logo.hAlign = 'LEFT'
        elements.append(logo)
    elements.append(Spacer(1, 20))
    elements.append(Paragraph("Factura de Compra", title_style))
    elements.append(Spacer(1, 20))

    # Detalles del pedido
    elements.append(Paragraph(f"<b>ID del Pedido:</b> {order.id}", normal_style))
    elements.append(Paragraph(f"<b>Fecha:</b> {order.created_at.strftime('%Y-%m-%d %H:%M:%S')}", normal_style))
    elements.append(Paragraph(f"<b>Total:</b> ${order.total:,.0f}".replace(",", "."), normal_style))
    elements.append(Spacer(1, 20))

    # Productos
    elements.append(Paragraph("Productos:", subtitle_style))
    table_data = [["Producto", "Cantidad", "Precio Unitario", "Total"]]

    for item in order.items.all():
        table_data.append([
            item.product.name,
            str(item.quantity),
            f"${item.product.price:,.0f}".replace(",", "."),
            f"${item.product.price * item.quantity:,.0f}".replace(",", "."),
        ])

    # Tabla de productos
    table = Table(table_data, colWidths=[200, 70, 100, 100])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#f2f2f2")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor("#333333")),
        ('ALIGN', (1, 1), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ]))
    elements.append(table)

    # Espaciado final
    elements.append(Spacer(1, 40))
    elements.append(Paragraph("&copy; 2024 Seifer - Jabones Reciclados. Gracias por tu compra.", normal_style))

    # Construir el documento
    doc.build(elements)
    buffer.seek(0)
    return buffer

def process_order(request):
    if request.method == 'POST':
        # Obtener el carrito del usuario (puedes ajustar según tu lógica)
        cart = get_object_or_404(Cart, user=request.user)

        # Procesar cada ítem en el carrito
        with transaction.atomic():  # Asegura que la operación sea atómica
            for item in cart.items.all():
                product = item.product
                if product.stock >= item.quantity:
                    # Reducir el stock
                    product.stock -= item.quantity
                    product.save()
                else:
                    # Opcional: manejar casos donde no hay suficiente stock
                    return render(request, 'store/insufficient_stock.html', {
                        'product': product
                    })

        # Vaciar el carrito después del procesamiento
        cart.items.all().delete()

        # Redirigir a una página de éxito
        return render(request, 'store/order_success.html')