# Generated by Django 4.2.1 on 2023-09-15 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0004_remove_product_image_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='Product_image',
        ),
    ]
