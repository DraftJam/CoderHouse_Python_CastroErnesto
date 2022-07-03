from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic import DetailView, CreateView

from posts.models import Profile
from .forms import EditProfileForm, UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from logeo.forms import ProfilePageForm
# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class= UserCreationForm
    template_name= "register.html"
    success_url = reverse_lazy('login')

def inicio(request):
    return render(request, "padre.html")

class UserEditView(generic.UpdateView):
    form_class= EditProfileForm
    template_name= "edit_profile.html"
    success_url = reverse_lazy('inicio')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('inicio')

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context ["page_user"] = page_user
        return context

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'edit_profile_page.html'
    fields = ['bio', 'website_url', 'profile_pic']
    success_url = reverse_lazy('inicio')

class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = "create_user_profile_page.html"
    #fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
def about(request):
    return render(request, "about.html")

