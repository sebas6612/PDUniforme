# Generated by Django 2.0 on 2017-12-28 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colegio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedidoCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_solicitada', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('cantidad_entregada', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6)),
                ('cantidad_entregada_anterior', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6)),
                ('precio_venta', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
            ],
            options={
                'verbose_name': 'Detalle pedido',
                'verbose_name_plural': 'Detalle pedido',
            },
        ),
        migrations.CreateModel(
            name='PedidoCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pedido', models.DateField(auto_now=True)),
                ('cantidad', models.IntegerField(blank=True, default=0)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clientes.Colegio')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedido',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.PositiveIntegerField(unique=True, verbose_name='Código')),
                ('nombre', models.CharField(max_length=120)),
                ('fecha_vencimiento', models.DateField(verbose_name='Fecha de vencimiento')),
                ('stock', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Cantidad disponible')),
                ('unidad_de_medida', models.CharField(choices=[('KG', 'Kilogramos'), ('LT', 'Litros'), ('UN', 'Unidades')], max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='detallepedidocliente',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clientes.PedidoCliente'),
        ),
        migrations.AddField(
            model_name='detallepedidocliente',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clientes.Producto'),
        ),
    ]
