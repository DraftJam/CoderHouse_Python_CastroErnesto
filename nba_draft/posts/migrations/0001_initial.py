# Generated by Django 4.0.4 on 2022-06-26 20:27

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('modelobase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.modelobase')),
                ('titulo', models.CharField(max_length=150, unique=True, verbose_name='Titulo del Post')),
                ('slug', models.CharField(max_length=150, unique=True, verbose_name='Slug')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
                ('contenido', ckeditor.fields.RichTextField()),
                ('imagen_referencial', models.ImageField(max_length=255, upload_to='imagenes/', verbose_name='Imagen referencial')),
                ('fecha_publicacion', models.DateField(verbose_name='fecha de publicacion')),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
            bases=('users.modelobase',),
        ),
    ]
