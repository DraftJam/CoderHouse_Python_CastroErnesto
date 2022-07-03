#from unittest import loader
#from django.http import HttpResponse
#from django.shortcuts import render
from django.urls import reverse_lazy
from posts.models import Post, Comment
#from django.template import loader
#from posts.forms import Post_formulario
#from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
#from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from posts.forms import AddCommentForm

# Create your views here.


class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'

class Lista(ListView):
    model = Post
    template_name = 'lista.html'

class Detalle(DetailView):
    model = Post
    template_name = 'detalle.html' 

class UpdatePostView(UpdateView):
    model = Post
    template_name= 'update_post.html'
    fields = ['titulo','descripcion','contenido', 'imagen_referencial']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('inicio')

class AddCommentView(CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = 'add_comment.html'
    #fields = '__all__'
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.name = self.request.user.username
        return super().form_valid(form)

    success_url = reverse_lazy('inicio')
    def get_success_url(self):
        return reverse_lazy('detalle', kwargs={'pk': self.kwargs['pk']})

