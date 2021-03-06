# Generated by Django 2.1.3 on 2018-11-24 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='2018-11-24 11:07:19.364753', max_length=255, unique=True)),
                ('historia', models.TextField()),
                ('historiaImagen', models.ImageField(upload_to='images')),
            ],
            options={
                'verbose_name_plural': 'Historias',
            },
        ),
        migrations.CreateModel(
            name='Mision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='2018-11-24 11:07:19.367747', max_length=255, unique=True)),
                ('mision', models.TextField()),
                ('imagen', models.ImageField(upload_to='images')),
            ],
            options={
                'verbose_name_plural': 'Misiones',
            },
        ),
        migrations.CreateModel(
            name='Somos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='2018-11-24 11:07:19.363755', max_length=255, unique=True)),
                ('titulo', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Titulos',
            },
        ),
        migrations.CreateModel(
            name='Valor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='2018-11-24 11:07:19.358768', max_length=255, unique=True)),
                ('valor', models.TextField()),
                ('valoresImagen', models.ImageField(upload_to='images')),
            ],
            options={
                'verbose_name_plural': 'Valores',
            },
        ),
    ]
