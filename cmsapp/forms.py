from django import forms
from cmsapp.models import Product
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, required=True, widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label=("Password"), widget=forms.PasswordInput)

class Product(forms.ModelForm):
    title=forms.CharField(max_length=50)
    details=forms.CharField(max_length=100)
    cost=forms.IntegerField()

    class Meta:
        model=Product
        fields=['title','details','cost']
