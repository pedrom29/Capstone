from django.urls import path
from . import views
from .views import react_view
from .views import product_list_json
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.product_list, name='product_list'),  # Ruta para listar productos
    path('product/<int:pk>/', views.product_detail, name='product_detail'),  # Detalle de producto
    path('cart/', views.cart_detail, name='cart_detail'),  # Ver el carro
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  # Agregar al carro
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),  # Eliminar del carro
    path('', views.product_list, name='product_list'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment/<int:order_id>/', views.payment, name='payment'),  # Para Webpay    
    path('webpay/initiate/<int:order_id>/', views.webpay_initiate, name='webpay_initiate'),    
    path('webpay/response/', views.webpay_response, name='webpay_response'),
    path('cart/item/<int:item_id>/<str:action>/', views.update_cart_item, name='update_cart_item'),
    path('send_confirmation_email/', views.send_confirmation_email, name='send_confirmation_email'),
    path('download_invoice_pdf/', views.download_invoice_pdf, name='download_invoice_pdf'),
    path('', react_view, name='react_view'),  # Todas las rutas servirán React
    path('api/products/', product_list_json, name='product_list_json'),
    path('', views.base, name='home'),
    path('register/', views.register_view, name='register'),
    path('products/', views.product_list, name='product_list'),  # Página de productos

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
