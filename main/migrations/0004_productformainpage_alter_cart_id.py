# Generated by Django 4.2.1 on 2023-05-26 18:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_fabric_addition_to_price_alter_cart_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductForMainPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pic', models.FileField(upload_to='img', verbose_name='img')),
            ],
        ),
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.UUIDField(default=uuid.UUID('2e0cbb66-328d-440e-880e-318499a36e27'), primary_key=True, serialize=False),
        ),
    ]
