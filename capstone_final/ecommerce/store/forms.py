from django import forms
from django.contrib.auth.models import User
from datetime import date, timedelta
from store.models import Profile  # Asegúrate de que este modelo está definido

class UserRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(required=True, label="Nombre", max_length=30)
    last_name = forms.CharField(required=True, label="Apellidos", max_length=30)
    rut = forms.CharField(required=True, label="RUT", max_length=12)  # Campo obligatorio
    email = forms.EmailField(required=True, label="Correo Electrónico")
    phone = forms.CharField(required=True, label="Teléfono", max_length=15)
    password = forms.CharField(required=True, widget=forms.PasswordInput, label="Contraseña")
    confirm_password = forms.CharField(required=True, widget=forms.PasswordInput, label="Confirmar Contraseña")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        # Validación adicional para RUT
        rut = cleaned_data.get("rut")
        if rut:  # Solo validar si el RUT no es None
            if not rut.isdigit() or len(rut) not in range(8, 13):
                raise forms.ValidationError("El RUT debe contener entre 8 y 12 caracteres numéricos.")
        else:
            raise forms.ValidationError("El campo RUT es obligatorio.")

        return cleaned_data


class OrderForm(forms.Form):
    address = forms.CharField(label="Dirección", max_length=255, required=True)
    comuna = forms.CharField(label="Comuna", max_length=100, required=True)
    city = forms.CharField(label="Ciudad", max_length=100, required=True)
    phone = forms.CharField(label="Teléfono", max_length=15, required=True)
    delivery_date = forms.DateField(label="Fecha de Entrega", widget=forms.SelectDateWidget)

    def clean_delivery_date(self):
        delivery_date = self.cleaned_data.get("delivery_date")
        today = date.today()
        max_date = today + timedelta(days=7)
        
        if delivery_date < today:
            raise forms.ValidationError("La fecha no puede ser anterior a hoy.")
        
        if delivery_date > max_date:
            raise forms.ValidationError("La fecha no puede superar los próximos 7 días hábiles.")

        return delivery_date
