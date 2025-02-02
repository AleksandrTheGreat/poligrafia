# Generated by Django 4.2 on 2023-10-25 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=254, verbose_name='Эл.Почта')),
                ('workphone', models.CharField(max_length=20, verbose_name='Раб.Телефон')),
                ('mobilephone', models.CharField(max_length=20, verbose_name='Сот.Телефон')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
                ('cena', models.IntegerField(verbose_name='Цена')),
                ('image', models.CharField(max_length=100, verbose_name='Картинка')),
            ],
        ),
    ]
