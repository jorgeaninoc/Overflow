# Generated by Django 2.1.1 on 2018-11-19 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Colabora', '0003_auto_20181119_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaboraimagen',
            name='nombre',
            field=models.CharField(default='2018-11-19 04:27:04.006712', max_length=255, unique=True),
        ),
    ]
