# Generated by Django 2.1 on 2019-10-26 19:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scmi', '0014_auto_20191026_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 26, 14, 39, 51, 31141)),
        ),
        migrations.AlterField(
            model_name='factura',
            name='fecventa',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 26, 14, 39, 51, 41142)),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='fechaingreso',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 26, 14, 39, 51, 26140)),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecentrega',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 26, 14, 39, 51, 35141)),
        ),
        migrations.AlterField(
            model_name='proforma',
            name='fec',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 26, 14, 39, 51, 42142)),
        ),
    ]
