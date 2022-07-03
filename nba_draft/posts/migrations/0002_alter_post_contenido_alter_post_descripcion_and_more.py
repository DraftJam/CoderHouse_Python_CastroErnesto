# Generated by Django 4.0.4 on 2022-06-26 23:05

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contenido',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='descripcion',
            field=models.TextField(verbose_name='descripcion'),
        ),
        migrations.AlterField(
            model_name='post',
            name='fecha_publicacion',
            field=models.DateField(auto_now=True, verbose_name='fecha de publicacion'),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagen_referencial',
            field=models.ImageField(max_length=255, null=True, upload_to='imagenes/', verbose_name='imagen referencial'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=150, unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=150, unique=True, verbose_name='titulo'),
        ),
    ]
