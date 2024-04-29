# Generated by Django 5.0.4 on 2024-04-28 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Сумма позиции'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Количетсво'),
        ),
    ]
