# Generated by Django 5.0.4 on 2024-04-28 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_is_received'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='is_received',
            new_name='is_confirmed',
        ),
    ]
