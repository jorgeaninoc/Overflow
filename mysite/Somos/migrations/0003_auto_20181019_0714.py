# Generated by Django 2.1.1 on 2018-10-19 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Somos', '0002_auto_20181018_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historia',
            name='nombre',
            field=models.CharField(default='2018-10-19 07:14:00.721540', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='mision',
            name='nombre',
            field=models.CharField(default='2018-10-19 07:14:00.722533', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='somos',
            name='nombre',
            field=models.CharField(default='2018-10-19 07:14:00.721540', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='valor',
            name='nombre',
            field=models.CharField(default='2018-10-19 07:14:00.720541', max_length=255, unique=True),
        ),
    ]