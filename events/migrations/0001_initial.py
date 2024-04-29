# Generated by Django 4.2.11 on 2024-04-29 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date_and_time', models.DateTimeField()),
                ('location', models.CharField(max_length=255)),
                ('organizer', models.CharField(max_length=255)),
            ],
        ),
    ]
