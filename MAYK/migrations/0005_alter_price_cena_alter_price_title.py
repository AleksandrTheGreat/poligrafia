# Generated by Django 4.2.6 on 2023-10-25 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAYK', '0004_alter_price_cena'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='cena',
            field=models.CharField(max_length=100, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='price',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
    ]
