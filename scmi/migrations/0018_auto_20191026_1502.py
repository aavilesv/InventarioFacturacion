# Generated by Django 2.1 on 2019-10-26 20:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scmi', '0017_auto_20191026_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 26, 15, 2, 29, 194406)),
        ),
        migrations.AlterField(
            model_name='factura',
            name='fecventa',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 26, 15, 2, 29, 202406)),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='fechaingreso',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 26, 15, 2, 29, 190405)),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecentrega',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 26, 15, 2, 29, 198406)),
        ),
        migrations.AlterField(
            model_name='proforma',
            name='fec',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 26, 15, 2, 29, 204407)),
        ),
    ]