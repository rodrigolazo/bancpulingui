# Generated by Django 3.1.1 on 2020-10-10 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_post_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='/imagen/banner/placeholder.png', null=True, upload_to='imagen'),
        ),
    ]