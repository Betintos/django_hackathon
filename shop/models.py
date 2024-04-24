from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, unique=True, verbose_name = 'Категория')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='Идентификатор в URL')

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    name = models.CharField(max_length=200, unique=True, db_index=True, verbose_name='Название')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Картинка')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    stock = models.PositiveIntegerField(verbose_name='Количество на складе')
    available = models.BooleanField(default=True, verbose_name='В наличии')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания!')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления!')

    class Meta:
        ordering = ['name']
        index_together = ['id']
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name