# Generated by Django 3.2.6 on 2021-08-21 21:40

import app.models.order
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210821_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_type',
            field=models.CharField(choices=[(app.models.order.OrderType['SELL'], 'SELL'), (app.models.order.OrderType['BUY'], 'BUY')], default='SELL', max_length=200),
        ),
    ]
