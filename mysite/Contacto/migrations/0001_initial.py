# Generated by Django 2.1.3 on 2018-11-24 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=255)),
                ('horario', models.CharField(max_length=255)),
                ('mail', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Informacion de Contacto',
            },
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('mensaje', models.TextField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Mensajes',
            },
        ),
    ]
