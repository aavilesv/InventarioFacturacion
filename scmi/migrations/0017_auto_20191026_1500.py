# Generated by Django 2.1 on 2019-10-26 20:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scmi', '0016_auto_20191026_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 26, 15, 0, 10, 615199)),
        ),
        migrations.AlterField(
            model_name='factura',
            name='fecventa',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 26, 15, 0, 10, 622199)),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='fechaingreso',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 26, 15, 0, 10, 611198)),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecentrega',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 26, 15, 0, 10, 619199)),
        ),
        migrations.AlterField(
            model_name='proforma',
            name='fec',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 26, 15, 0, 10, 623200)),
        ),
    ]
