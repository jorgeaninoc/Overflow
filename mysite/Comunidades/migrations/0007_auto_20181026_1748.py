# Generated by Django 2.1.1 on 2018-10-26 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comunidades', '0006_auto_20181019_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='nombre',
            field=models.CharField(default='2018-10-26 17:48:10.767856', max_length=255, unique=True),
        ),
    ]
