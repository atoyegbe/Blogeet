from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class createBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']
        exclude = ['creator']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
