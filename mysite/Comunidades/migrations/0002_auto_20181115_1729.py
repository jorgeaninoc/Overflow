# Generated by Django 2.1.1 on 2018-11-15 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comunidades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='nombre',
            field=models.CharField(default='2018-11-15 17:29:46.573085', max_length=255, unique=True),
        ),
    ]
