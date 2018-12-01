# Generated by Django 2.1.3 on 2018-11-24 17:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Comunidades', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='2018-11-24 11:07:14.077600', max_length=255, unique=True)),
                ('path', models.ImageField(upload_to='images')),
            ],
            options={
                'verbose_name_plural': 'Imagenes',
            },
        ),
        migrations.CreateModel(
            name='Ordenes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_referencia', models.UUIDField(default=uuid.uuid4)),
                ('nombre', models.CharField(max_length=255)),
                ('correo', models.EmailField(max_length=254)),
                ('monto_totalcompra', models.CharField(default='0', max_length=255)),
                ('Fecha_de_Compra', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Ordenes Pendientes',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('precio', models.IntegerField()),
                ('descripcion', models.CharField(default='', max_length=255)),
                ('subCat', models.CharField(max_length=255)),
                ('communidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Comunidades.Comunidad')),
                ('imagenes', models.ManyToManyField(to='Catalogo.Imagen')),
            ],
            options={
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='ProductosCheckout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=255)),
                ('cantidad', models.IntegerField()),
                ('total', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'ProductosCheckout',
            },
        ),
        migrations.AddField(
            model_name='ordenes',
            name='productos',
            field=models.ManyToManyField(to='Catalogo.ProductosCheckout'),
        ),
    ]
