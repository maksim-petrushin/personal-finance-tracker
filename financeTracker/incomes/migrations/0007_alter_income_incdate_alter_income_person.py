# Generated by Django 4.2.2 on 2023-07-14 01:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('incomes', '0006_alter_income_incdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='incDate',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 7, 14, 1, 38, 42, 684398)),
        ),
        migrations.AlterField(
            model_name='income',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pluses', to='incomes.appusers'),
        ),
    ]
