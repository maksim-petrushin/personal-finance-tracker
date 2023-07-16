# Generated by Django 4.2.2 on 2023-07-16 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('incomes', '0008_remove_income_description_remove_income_incdate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incAmount', models.FloatField(default=0)),
                ('category', models.CharField(max_length=64)),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='minuses', to='incomes.appusers')),
            ],
        ),
    ]