# Generated by Django 5.0.4 on 2024-04-19 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_cart_favourite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favourite',
            name='product',
        ),
        migrations.RemoveField(
            model_name='favourite',
            name='user',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Favourite',
        ),
    ]
