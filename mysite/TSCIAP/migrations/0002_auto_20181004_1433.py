# Generated by Django 2.1.1 on 2018-10-04 14:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('TSCIAP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaboraimagen',
            name='nombre',
            field=models.CharField(default='2018-10-04 14:33:42.083988', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='galeriaimagen',
            name='nombre',
            field=models.CharField(default='2018-10-04 14:33:42.083443', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='imagen',
            name='nombre',
            field=models.CharField(default='2018-10-04 14:33:42.050694', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='inicioimagen',
            name='nombre',
            field=models.CharField(default='2018-10-04 14:33:42.082909', max_length=255),
        ),
        migrations.AlterField(
            model_name='mision',
            name='nombre',
            field=models.CharField(default='2018-10-04 14:33:42.086363', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='fechaFin',
            field=models.DateField(default=datetime.datetime(2018, 11, 3, 14, 33, 42, 81166, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='fechaInicio',
            field=models.DateField(default=datetime.datetime(2018, 10, 4, 14, 33, 42, 81121, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='politica',
            name='nombre',
            field=models.CharField(default='2018-10-04 14:33:42.085033', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='somos',
            name='nombre',
            field=models.CharField(default='2018-10-04 14:33:42.085432', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='valor',
            name='nombre',
            field=models.CharField(default='2018-10-04 14:33:42.084501', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='vision',
            name='nombre',
            field=models.CharField(default='2018-10-04 14:33:42.085828', max_length=255, unique=True),
        ),
    ]
