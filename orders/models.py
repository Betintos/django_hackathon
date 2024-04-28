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
        blank=True,
    )
    ordered_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата заказа")
    total_amount = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Общая сумма заказа")
    status = models.CharField(max_length=20)


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
    quantity = models.PositiveIntegerField(max_length=100, verbose_name="Количетсво")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Сумма позиции")


class Address(models.Model):
    class Meta:
        db_table = "addresses"

    street = models.CharField(max_length=255, verbose_name="Улица")
    city = models.CharField(max_length=255, verbose_name="Город")
    country = models.CharField(max_length=255, verbose_name="Страна")
    zipcode = models.CharField(max_length=255, verbose_name="Почтовый индекс")
