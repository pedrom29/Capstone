from django.urls import path
from . import views_auth  # Vamos a crear vistas separadas para autenticación

urlpatterns = [
    path('register/', views_auth.register, name='register'),
    path('login/', views_auth.login_view, name='login'),
    path('logout/', views_auth.logout_view, name='logout'),
]
