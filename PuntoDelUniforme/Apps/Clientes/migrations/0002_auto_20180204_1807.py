# Generated by Django 2.0 on 2018-02-04 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallepedidocliente',
            name='pedido',
        ),
        migrations.RemoveField(
            model_name='detallepedidocliente',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='pedidocliente',
            name='cliente',
        ),
        migrations.AlterField(
            model_name='colegio',
            name='Nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='DetallePedidoCliente',
        ),
        migrations.DeleteModel(
            name='PedidoCliente',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]