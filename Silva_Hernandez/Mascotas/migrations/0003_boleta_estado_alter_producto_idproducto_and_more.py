# Generated by Django 4.1.2 on 2023-07-13 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mascotas', '0002_boleta_detalle_boleta'),
    ]

    operations = [
        migrations.AddField(
            model_name='boleta',
            name='estado',
            field=models.CharField(default='Procesando Pedido', max_length=20),
        ),
        migrations.AlterField(
            model_name='producto',
            name='idProducto',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='id de producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(blank=True, verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(blank=True, verbose_name='Stock'),
        ),
    ]