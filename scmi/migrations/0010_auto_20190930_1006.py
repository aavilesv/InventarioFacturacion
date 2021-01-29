# Generated by Django 2.1 on 2019-09-30 15:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scmi', '0009_auto_20190927_1008'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleProforma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(default='', max_length=150)),
                ('cantidad', models.IntegerField(default=0, verbose_name='cantidad')),
                ('total', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('status', models.BooleanField(default=True)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='scmi.Articulo')),
            ],
            options={
                'verbose_name_plural': 'DetalleProforma',
                'ordering': ['id'],
                'verbose_name': 'DetalleProforma',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=60, verbose_name='nombre')),
                ('cedula', models.CharField(default='', max_length=15, verbose_name='cedula')),
                ('direcion', models.CharField(default='', max_length=50, verbose_name='direccion')),
                ('celular', models.CharField(default='', max_length=50, verbose_name='celular')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Empresa dato',
                'ordering': ['cedula'],
                'verbose_name': 'Empresa dato',
            },
        ),
        migrations.CreateModel(
            name='Proforma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fec', models.DateTimeField(default=datetime.datetime(2019, 9, 30, 10, 6, 13, 136458))),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='scmi.Empresa')),
            ],
            options={
                'verbose_name_plural': 'Proforma',
                'ordering': ['id'],
                'verbose_name': 'Proforma',
            },
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 30, 10, 6, 13, 114457)),
        ),
        migrations.AlterField(
            model_name='factura',
            name='fecventa',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 30, 10, 6, 13, 135459)),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='fechaingreso',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 30, 10, 6, 13, 108456)),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecentrega',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 30, 10, 6, 13, 122457)),
        ),
        migrations.AddField(
            model_name='detalleproforma',
            name='proforma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='scmi.Proforma'),
        ),
    ]
