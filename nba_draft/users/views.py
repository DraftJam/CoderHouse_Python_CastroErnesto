from django.http import HttpResponse
from django.shortcuts import render
#from app_coder.models import Curso
#from django.template import loader
#from app_coder.forms import Curso_formulario, UserEditForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
#from django.contrib.auth import login, authenticate
#from django.contrib.auth.decorators import login_required

#from app_coder.models import Avatar

# Create your views here.

def register(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()
            return HttpResponse("Usuario creado")

    else:
        form = UserCreationForm()

    return render(request, "registro.html", {"form":form})