# Generated by Django 4.2.1 on 2023-05-29 15:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a10b2209-f66d-4998-8d57-aa1064471918'), primary_key=True, serialize=False),
        ),
    ]
