# Generated by Django 4.0.4 on 2022-07-02 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_post_autor_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fecha_publicacion',
            field=models.DateField(auto_now=True, verbose_name='fecha de publicacion'),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(max_length=255, null=True, upload_to='imagenes/profile/', verbose_name='imagen referencial'),
        ),
    ]
