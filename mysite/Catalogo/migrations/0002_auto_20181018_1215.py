# Generated by Django 2.1.1 on 2018-10-18 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='nombre',
            field=models.CharField(default='2018-10-18 12:15:06.744912', max_length=255, unique=True),
        ),
    ]
