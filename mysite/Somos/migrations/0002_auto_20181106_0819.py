# Generated by Django 2.1.1 on 2018-11-06 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Somos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historia',
            name='nombre',
            field=models.CharField(default='2018-11-06 08:19:44.299933', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='mision',
            name='nombre',
            field=models.CharField(default='2018-11-06 08:19:44.299933', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='somos',
            name='nombre',
            field=models.CharField(default='2018-11-06 08:19:44.299933', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='valor',
            name='nombre',
            field=models.CharField(default='2018-11-06 08:19:44.298873', max_length=255, unique=True),
        ),
    ]
