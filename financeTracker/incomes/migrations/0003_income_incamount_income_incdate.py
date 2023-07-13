# Generated by Django 4.2.2 on 2023-07-13 12:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incomes', '0002_rename_destination_income_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='incAmount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='income',
            name='incDate',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 7, 13, 12, 7, 46, 152221)),
        ),
    ]
