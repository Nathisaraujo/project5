# Generated by Django 4.2.11 on 2024-05-29 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_learn_more_link1_post_learn_more_link2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='learn_more_text1',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Learn More Text 1'),
        ),
        migrations.AddField(
            model_name='post',
            name='learn_more_text2',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Learn More Text 2'),
        ),
        migrations.AddField(
            model_name='post',
            name='learn_more_text3',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Learn More Text 3'),
        ),
        migrations.AlterField(
            model_name='post',
            name='learn_more_link1',
            field=models.URLField(blank=True, null=True, verbose_name='Learn More Link 1'),
        ),
        migrations.AlterField(
            model_name='post',
            name='learn_more_link2',
            field=models.URLField(blank=True, null=True, verbose_name='Learn More Link 2'),
        ),
        migrations.AlterField(
            model_name='post',
            name='learn_more_link3',
            field=models.URLField(blank=True, null=True, verbose_name='Learn More Link 3'),
        ),
    ]
