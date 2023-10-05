from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'"Магазин Чая" ваш заказ № {order.id}'
    message = f'Дорогой {order.first_name}, \n\n' \
              f'Заказ успешно сформирован.' \
              f'Ваш номер заказа: {order.id}.'
    mail_sent = send_mail(subject,
                          message,
                          'urmanov.pro@gmail.com',
                          [order.email])
    return mail_sent
