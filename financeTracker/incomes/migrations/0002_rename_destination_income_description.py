# Generated by Django 4.2.2 on 2023-07-13 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incomes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='income',
            old_name='destination',
            new_name='description',
        ),
    ]
