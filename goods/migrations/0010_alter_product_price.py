# Generated by Django 5.0.4 on 2024-04-26 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0009_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Цена'),
        ),
    ]