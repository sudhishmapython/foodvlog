# Generated by Django 3.2.11 on 2022-04-13 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='product',
            new_name='prodct',
        ),
    ]
