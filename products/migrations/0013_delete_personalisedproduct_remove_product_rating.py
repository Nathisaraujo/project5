# Generated by Django 4.2.11 on 2024-05-14 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_delete_bundle'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PersonalisedProduct',
        ),
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
    ]
