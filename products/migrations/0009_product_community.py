# Generated by Django 4.2.11 on 2024-04-25 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_personalisedproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='community',
            field=models.BooleanField(default=False),
        ),
    ]
