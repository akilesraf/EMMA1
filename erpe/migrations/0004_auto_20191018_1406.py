# Generated by Django 2.2.4 on 2019-10-18 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erpe', '0003_auto_20191018_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='informe',
            name='Nombre_Apellido',
        ),
        migrations.RemoveField(
            model_name='informe',
            name='Numero_Pedido',
        ),
        migrations.AddField(
            model_name='informe',
            name='Numero_Producto',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='informe',
            name='Emil',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='informe',
            name='Telefono',
            field=models.CharField(max_length=50),
        ),
    ]
