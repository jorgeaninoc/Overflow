# Generated by Django 2.1.1 on 2018-11-05 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comunidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Comunidades',
            },
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='2018-11-05 11:14:23.085656', max_length=255, unique=True)),
                ('path', models.ImageField(upload_to='images')),
            ],
            options={
                'verbose_name_plural': 'Imagenes',
            },
        ),
        migrations.AddField(
            model_name='comunidad',
            name='imagenes',
            field=models.ManyToManyField(to='Comunidades.Imagen'),
        ),
    ]
