from django.contrib import admin
from .models import Product, Cart, CartItem, Category
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Profile

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)

# Extender el modelo de Usuario para incluir el modelo de Perfil
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Perfiles'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline]

    # Mostrar los campos adicionales en la lista de usuarios
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_rut', 'get_phone', 'is_staff')
    list_select_related = ('profile',)

    # Métodos para acceder a los campos extendidos del perfil
    def get_rut(self, instance):
        return instance.profile.rut
    get_rut.short_description = 'RUT'

    def get_phone(self, instance):
        return instance.profile.phone
    get_phone.short_description = 'Teléfono'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    search_fields = ('name', 'description')
    list_filter = ('category',)
@admin.register(Category)    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
# Re-registrar el modelo User con las nuevas configuraciones
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)