from django import template

register = template.Library()

@register.filter
def format_price(value):
    try:
        # Asegúrate de que el valor sea un número
        value = int(value)
        # Formatea el número con separación de miles
        return f"${value:,}".replace(",", ".")
    except (ValueError, TypeError):
        return value
