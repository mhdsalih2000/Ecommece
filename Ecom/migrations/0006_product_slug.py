# Generated by Django 4.2.5 on 2023-09-20 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0005_rename_image_product_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
