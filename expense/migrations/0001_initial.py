# Generated by Django 5.0 on 2023-12-06 14:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('description', models.CharField(max_length=50, verbose_name='descrição')),
                ('payment_date', models.DateField(blank=True, null=True, verbose_name='data de pagamento')),
                ('value', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='valor')),
                ('paid', models.BooleanField(default=False, verbose_name='pago')),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='expenses', to='crm.person', verbose_name='pago a')),
            ],
            options={
                'verbose_name': 'despesa',
                'verbose_name_plural': 'despesas',
                'ordering': ('-payment_date',),
            },
        ),
    ]