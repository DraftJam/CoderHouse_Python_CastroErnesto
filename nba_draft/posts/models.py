from django.db import models
from ckeditor.widgets import *
from ckeditor.fields import RichTextField
from users.models import ModeloBase
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Post (ModeloBase):
    titulo = models.CharField('titulo', max_length=150, unique=True)
    descripcion = models.TextField('descripcion')
    autor = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE, null=True)
    contenido = RichTextField()
    #contenido = models.TextField('contenido')
    imagen_referencial = models.ImageField('imagen referencial', upload_to = 'imagenes/', max_length = 255, null =True)
    fecha_publicacion = models.DateField('fecha de publicacion', auto_now=True)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('inicio')
        #return reverse('add_post', args=(str(self.id)))

class Comment(models.Model):

    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.titulo, self.name)

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    website_url = models.CharField(max_length=255, null = True, blank = True )
    profile_pic = models.ImageField('imagen referencial', upload_to = 'imagenes/profile/', max_length = 255, null =True)
    fecha_publicacion = models.DateField('fecha de publicacion', auto_now=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('inicio')
        #return reverse('add_post', args=(str(self.id)))

class Venue (models.Model):
    name = models.CharField('venue name', max_length=255, null = True, blank=True)
    image = models.ImageField(upload_to = "pics/")

    def __str__(self):
        return self.name