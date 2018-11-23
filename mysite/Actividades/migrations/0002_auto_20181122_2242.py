# Generated by Django 2.1.1 on 2018-11-22 22:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Actividades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='nombre',
            field=models.CharField(default='2018-11-22 22:42:47.617516', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='fechaFin',
            field=models.DateField(default=datetime.datetime(2018, 12, 22, 22, 42, 47, 628641, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='fechaInicio',
            field=models.DateField(default=datetime.datetime(2018, 11, 22, 22, 42, 47, 618236, tzinfo=utc)),
        ),
    ]
