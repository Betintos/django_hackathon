from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_order_confirmation_code(email, confirmation_code):
    context = {
        "text_detail": "Спасибо за оформление заказа",
        "email": email,
        "domain": "http://localhost:8000",
        "confirmation_code": confirmation_code,
    }
    msg_html = render_to_string("order_confirmation.html", context)
    message = strip_tags(msg_html)
    send_mail(
        "Order confirmation",
        message,
        "admin@admin.com",
        [email],
        html_message=msg_html,
        fail_silently=False,
    )
