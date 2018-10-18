# Generated by Django 2.1.1 on 2018-10-18 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Comunidades', '0002_auto_20181018_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='2018-10-18 11:08:20.512274', max_length=255, unique=True)),
                ('path', models.ImageField(upload_to='images')),
            ],
            options={
                'verbose_name_plural': 'Imagenes',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('precio', models.IntegerField()),
                ('subCat', models.CharField(max_length=255)),
                ('communidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Comunidades.Comunidad')),
                ('imagenes', models.ManyToManyField(to='Catalogo.Imagen')),
            ],
            options={
                'verbose_name_plural': 'Productos',
            },
        ),
    ]
