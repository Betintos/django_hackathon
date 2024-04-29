from django.db import models
from django.contrib.auth import get_user_model


from goods.models import Product


User = get_user_model()


class Order(models.Model):
    class Meta:
        db_table = "orders"

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="orders",
        verbose_name="Заказчик",
    )
    ordered_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата заказа")
    total_amount = models.DecimalField(default=0, max_digits=7, decimal_places=2, verbose_name="Общая сумма заказа", blank=True)
    status = models.CharField(max_length=20, blank=True)
    is_confirmed = models.BooleanField(default=False)
    confirmation_code = models.CharField(max_length=10, blank=True)

    


class OrderDetail(models.Model):
    class Meta:
        db_table = "order_details"

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="order_details",
        verbose_name="Номер заказа",
        blank=True,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Номер товара",
        blank=True,
    )
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количетсво")
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name="Сумма позиции")


class Address(models.Model):
    class Meta:
        db_table = "addresses"

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Заказчик")
    street = models.CharField(max_length=255, verbose_name="Улица", blank=True)
    city = models.CharField(max_length=255, verbose_name="Город", blank=True)
    country = models.CharField(max_length=255, verbose_name="Страна", blank=True)
    zipcode = models.CharField(max_length=255, verbose_name="Почтовый индекс", blank=True)
