from django.urls import path
from . import views
from .views import react_view, product_list_json
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),  # Página principal
    path('products/', views.product_list, name='product_list'),  # Página de productos
    path('product/<int:pk>/', views.product_detail, name='product_detail'),  # Detalle de producto
    path('cart/', views.cart_detail, name='cart_detail'),  # Ver el carro
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  # Agregar al carro
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),  # Eliminar del carro
    path('checkout/', views.checkout, name='checkout'),  # Checkout
    path('payment/<int:order_id>/', views.payment, name='payment'),  # Para Webpay
    path('webpay/initiate/<int:order_id>/', views.webpay_initiate, name='webpay_initiate'),    
    path('webpay/response/', views.webpay_response, name='webpay_response'),
    path('cart/item/<int:item_id>/<str:action>/', views.update_cart_item, name='update_cart_item'),  # Actualizar item del carro
    path('send_confirmation_email/', views.send_confirmation_email, name='send_confirmation_email'),  # Enviar correo
    path('download_invoice_pdf/', views.download_invoice_pdf, name='download_invoice_pdf'),  # Descargar PDF
    path('react/', react_view, name='react_view'),  # Sirve React en una ruta específica
    path('api/products/', product_list_json, name='product_list_json'),  # API de productos
    path('register/', views.register_view, name='register'),  # Registro de usuario
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
