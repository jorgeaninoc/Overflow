# Generated by Django 2.1.1 on 2018-10-29 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Colabora', '0008_auto_20181029_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaboraimagen',
            name='nombre',
            field=models.CharField(default='2018-10-29 09:44:16.275213', max_length=255, unique=True),
        ),
    ]
