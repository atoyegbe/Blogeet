from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class createBlog(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ['creator', 'slug']
class profileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

