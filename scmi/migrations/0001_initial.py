# Generated by Django 2.2.4 on 2019-08-13 07:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=200, verbose_name='articulo')),
                ('descripcion', models.CharField(default='', max_length=200, verbose_name='descripción')),
                ('cantidad', models.IntegerField(default=0, verbose_name='cantidad')),
                ('iva', models.DecimalField(decimal_places=2, default=0.12, max_digits=19, verbose_name='iva')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0, max_digits=19, verbose_name='subtotal')),
                ('precio', models.DecimalField(decimal_places=2, default=0, max_digits=19, verbose_name='Precio')),
            ],
            options={
                'verbose_name': 'Inventariosalidacompra',
                'ordering': ['nombre'],
                'verbose_name_plural': 'salidacompra',
            },
        ),
        migrations.CreateModel(
            name='CliProentidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=200, verbose_name='EMPRESA')),
                ('tipo', models.IntegerField(choices=[(1, 'Cliente'), (2, 'Proveedor')], default=0)),
                ('direccion', models.CharField(default='', max_length=200, verbose_name='DIRECCION')),
                ('telefono', models.CharField(default='', max_length=200, verbose_name='TELEFONO')),
                ('ced_ruc', models.CharField(default='', max_length=200, verbose_name='Cedula o Ruc')),
            ],
            options={
                'verbose_name': 'CliProentidad',
                'ordering': ['nombre'],
                'verbose_name_plural': 'CliCliprov',
            },
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 13, 2, 38, 3, 377578))),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
                ('CliProentidad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='scmi.CliProentidad')),
            ],
            options={
                'verbose_name': 'Inventariosalidacompra',
                'ordering': ['id'],
                'verbose_name_plural': 'salidacompra',
            },
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaingreso', models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 13, 2, 38, 3, 374575))),
                ('fechasalida', models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 13, 2, 38, 3, 375575))),
                ('cantidad', models.IntegerField(default=0)),
                ('saldo', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Inventario General vale',
                'ordering': ['material'],
                'verbose_name_plural': 'Inventario General vale',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(default='', max_length=5)),
                ('fecentrega', models.DateTimeField(default=datetime.datetime(2019, 8, 13, 2, 38, 3, 382575))),
                ('coutainicial', models.DecimalField(decimal_places=2, default=0, max_digits=19, verbose_name='coutainicial')),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='scmi.Articulo')),
            ],
            options={
                'verbose_name': 'Pedido',
                'ordering': ['id'],
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='TipoMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, default=' ', max_length=100)),
            ],
            options={
                'verbose_name': 'TipoMaterial vale',
                'ordering': ['nombre'],
                'verbose_name_plural': 'TipoMaterialesvale',
            },
        ),
        migrations.CreateModel(
            name='Pedidodetalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0, verbose_name='cantidad')),
                ('inventario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='scmi.Inventario')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='scmi.Pedido')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(default=' ', max_length=200)),
                ('arprecio', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
                ('tipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='scmi.TipoMaterial')),
            ],
            options={
                'verbose_name': 'Materialll',
                'ordering': ['material'],
                'verbose_name_plural': 'Materialll',
            },
        ),
        migrations.AddField(
            model_name='inventario',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='scmi.Material'),
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecventa', models.DateTimeField(default=datetime.datetime(2019, 8, 13, 2, 38, 3, 384576))),
                ('iva', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='scmi.CliProentidad')),
            ],
            options={
                'verbose_name': 'Pedido',
                'ordering': ['id'],
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='Detfactura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0, verbose_name='cantidad')),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='scmi.Articulo')),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='scmi.Factura')),
            ],
        ),
        migrations.CreateModel(
            name='Comprainventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0)),
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
                ('Inventario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='scmi.Inventario')),
                ('salidacompra', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='scmi.Compra')),
            ],
            options={
                'verbose_name': 'Inventariosalidacompra',
                'ordering': ['id'],
                'verbose_name_plural': 'salidacompra',
            },
        ),
    ]