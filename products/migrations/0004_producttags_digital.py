# Generated by Django 3.2.25 on 2024-04-08 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20240408_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttags',
            name='digital',
            field=models.BooleanField(default=False),
        ),
    ]