from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Upload
class RegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta:
        model= User
        fields = ['username', 'email','password1','password2',]

class uploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields=['title','Upload_File','Upload_Image']