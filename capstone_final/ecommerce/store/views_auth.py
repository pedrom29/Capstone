from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import Cart, Profile
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Crear el usuario
            user = User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )

          

            # Transferir el carrito del invitado al nuevo usuario
            session_id = request.session.session_key
            if session_id:
                guest_cart = Cart.objects.filter(session_id=session_id).first()
                if guest_cart:
                    guest_cart.user = user
                    guest_cart.session_id = None  # Eliminar el session_id
                    guest_cart.save()

            # Iniciar sesión automáticamente después del registro
            login(request, user)
            messages.success(request, 'Te has registrado correctamente. Tus productos fueron guardados.')
            return redirect('cart_detail')
    else:
        form = UserRegistrationForm()

    return render(request, 'store/register.html', {'form': form})

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # Crear el perfil solo si el usuario es nuevo y no tiene perfil
    if created and not Profile.objects.filter(user=instance).exists():
        Profile.objects.create(user=instance)

#Inicio de Sesión
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Has iniciado sesión correctamente.')
            return redirect('product_list')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
            return redirect('login')

    return render(request, 'store/login.html')

#Cerrar Sesión
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión correctamente.')
    return redirect('login')
