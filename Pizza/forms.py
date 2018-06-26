from django.forms import ModelForm
from Pizza.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class IngredientsForm(ModelForm):
    class Meta:
        model = Ingredients
        fields = ['name','description','image','code','price',]

class MassForm(ModelForm):
    class Meta:
        model = Mass
        fields = ['name','description','image','code','price',]

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields =['name','birthday','email','directions','rut','dv',]


class DirectionForm(ModelForm):
    class Meta:
        model = Direction
        fields =["name_street","number_street","city","commune"]

class ClientUserForm(ModelForm):

    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','password1', 'password2', )