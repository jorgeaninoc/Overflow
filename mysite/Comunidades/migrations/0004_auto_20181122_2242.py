# Generated by Django 2.1.1 on 2018-11-22 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comunidades', '0003_auto_20181121_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='nombre',
            field=models.CharField(default='2018-11-22 22:42:47.153609', max_length=255, unique=True),
        ),
    ]
