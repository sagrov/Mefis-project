# Generated by Django 4.2.1 on 2023-05-28 19:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_categories_slug_product_slug_subcategories_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.UUIDField(default=uuid.UUID('acca88ec-6525-4ec7-8464-ca4e98123f93'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='aboba-product', max_length=100, null=True),
        ),
    ]