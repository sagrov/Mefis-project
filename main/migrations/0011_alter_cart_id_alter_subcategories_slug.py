# Generated by Django 4.2.1 on 2023-05-28 19:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_cart_id_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.UUIDField(default=uuid.UUID('2220043c-d3f8-4c49-b1b8-048de7abc6ec'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subcategories',
            name='slug',
            field=models.SlugField(default='aboba-sub', max_length=100, null=True),
        ),
    ]