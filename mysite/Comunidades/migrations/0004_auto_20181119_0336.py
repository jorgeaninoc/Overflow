# Generated by Django 2.1.1 on 2018-11-19 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comunidades', '0003_auto_20181115_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='nombre',
            field=models.CharField(default='2018-11-19 03:35:39.906551', max_length=255, unique=True),
        ),
    ]
