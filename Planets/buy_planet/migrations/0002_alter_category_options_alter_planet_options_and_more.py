# Generated by Django 4.1.7 on 2023-03-19 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buy_planet', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='planet',
            options={'verbose_name': 'Планета', 'verbose_name_plural': 'Планеты'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='cat',
        ),
    ]
