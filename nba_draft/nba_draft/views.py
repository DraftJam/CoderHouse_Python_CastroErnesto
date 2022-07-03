#from unittest import loader
#from django.http import HttpResponse
from django.shortcuts import render
from posts.models import Post
#from django.template import loader
#from posts.forms import Post_formulario
#from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
#from django.contrib.auth import login, authenticate
#from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView

# Create your views here.

def detalle(request):
    return render(request, "detalle.html")

def inicio(request):
    return render(request, "padre.html")

def about(request):
    return render(request, "about.html")