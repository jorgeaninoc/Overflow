# Generated by Django 2.1.1 on 2018-11-19 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Somos', '0003_auto_20181119_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historia',
            name='nombre',
            field=models.CharField(default='2018-11-19 04:27:04.027032', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='mision',
            name='nombre',
            field=models.CharField(default='2018-11-19 04:27:04.027757', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='somos',
            name='nombre',
            field=models.CharField(default='2018-11-19 04:27:04.026457', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='valor',
            name='nombre',
            field=models.CharField(default='2018-11-19 04:27:04.024586', max_length=255, unique=True),
        ),
    ]