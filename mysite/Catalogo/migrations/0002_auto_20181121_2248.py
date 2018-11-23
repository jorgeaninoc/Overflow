# Generated by Django 2.1.1 on 2018-11-22 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imagen',
            name='nombre',
            field=models.CharField(default='2018-11-21 22:48:11.723368', max_length=255, unique=True),
        ),
    ]
