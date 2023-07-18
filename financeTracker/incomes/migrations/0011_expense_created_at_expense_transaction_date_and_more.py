# Generated by Django 4.2.2 on 2023-07-17 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incomes', '0010_rename_incamount_expense_expamount'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='created_at',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='expense',
            name='transaction_date',
            field=models.DateTimeField(db_comment='Date when transaction happened', default=None),
        ),
        migrations.AddField(
            model_name='expense',
            name='updates_at',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='income',
            name='created_at',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='income',
            name='transaction_date',
            field=models.DateTimeField(db_comment='Date when transaction happened', default=None),
        ),
        migrations.AddField(
            model_name='income',
            name='updates_at',
            field=models.DateTimeField(default=None),
        ),
    ]