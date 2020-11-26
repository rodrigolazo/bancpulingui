# Generated by Django 3.1.1 on 2020-10-16 07:29

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_institucion'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoticiaInicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombres')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Descripcion')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Contenido')),
                ('image', models.ImageField(blank=True, default='placeholder.png', null=True, upload_to='noticia-inicio', verbose_name='Imagen')),
                ('date', models.DateField(auto_now_add=True)),
                ('active', models.BooleanField(default=False, verbose_name='Activar')),
            ],
        ),
    ]