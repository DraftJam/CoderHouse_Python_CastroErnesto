from turtle import textinput
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from posts.models import Profile

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs ={'class': 'form-control'}))
    first_name = forms.CharField( max_length=100, widget = forms.TextInput(attrs = {'class': 'form-control'}))
    last_name = forms.CharField( max_length=100, widget = forms.TextInput(attrs = {'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields= ('bio', 'website_url', 'profile_pic')
        widgets = {
            'bio': forms.Textarea(attrs ={ 'class': 'form-control'}),
            'website_url': forms.TextInput (attrs = {'class': 'form-comtrol'}),
            #'profile_pic': forms.ImageField (attrs ={'class': 'form-control'})
    }