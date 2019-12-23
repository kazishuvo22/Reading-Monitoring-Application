from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import pdf_file



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ['username', 'email','phone_no','password1', 'password2']


class uploadpdf(forms.ModelForm):
    class Meta:
        model = pdf_file
        fields = {'name','pdffile'}
