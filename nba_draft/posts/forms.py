from posts.models import Comment
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.fields import RichTextFormField
from django.forms import ModelForm, Textarea
from .models import Post


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {
            'body' : forms.Textarea ( attrs ={'class': 'form-control'})
        }



