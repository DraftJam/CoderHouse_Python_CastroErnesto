from django.db import models
#from django.contrib.auth.models import User
#from django import forms
#from users.forms import AutorCreationForm


# Create your models here.

class ModeloBase(models.Model):

    id= models.AutoField(primary_key=True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now = False, auto_now_add=True)