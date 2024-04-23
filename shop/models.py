from django.db import models


class Category(models.Moe):
    title = models.CharField(max_length=200, unique=True, db_index=True, verbose_name='Категория')

    