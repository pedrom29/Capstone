from django import template

register = template.Library()

@register.filter
def clp_format(value):
    """
    Formatea un número para mostrarlo como CLP.
    Ejemplo: 123456789 -> $123.456.789
    """
    try:
        value = int(value)  # Convertir a entero
        return f"${value:,.0f}".replace(",", ".")  # Formatear y reemplazar comas con puntos
    except (ValueError, TypeError):
        return value  # En caso de error, devolver el valor original




@register.filter
def add_dot_separator(value):
    try:
        if isinstance(value, (int, float)):
            return f"{value:,.0f}".replace(",", ".")
        return value
    except (ValueError, TypeError):
        return value
    

@register.filter(name='add_class')
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})

@register.filter
def add_dot_separator(value):
    """
    Agrega un punto como separador de miles y elimina los decimales.
    """
    try:
        # Convierte el valor a entero (sin decimales) y aplica el formato con puntos
        value = int(float(value))  # Asegúrate de convertir a entero
        return f"{value:,}".replace(",", ".")
    except (ValueError, TypeError):
        return value
    
