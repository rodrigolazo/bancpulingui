# Generated by Django 3.1.1 on 2020-10-14 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20201014_0208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Descripcion')),
                ('image', models.ImageField(blank=True, default='placeholder.png', null=True, upload_to='galeria', verbose_name='Imagen')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False, verbose_name='Activar')),
            ],
        ),
    ]
