from io import BytesIO
from reportlab.pdfgen import canvas

def generate_invoice_pdf(order):
    """
    Genera un archivo PDF en memoria para un pedido específico.
    """
    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    # Contenido del PDF
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
    buffer.seek(0)
    return buffer.getvalue()
