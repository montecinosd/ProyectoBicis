from django.forms import ModelForm
from Pizza.models import Ingredients, Mass, Client, Direction


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
        fields =['name','birthday','email','directions','user','rut','dv',]


class DirectionForm(ModelForm):
    class Meta:
        model = Direction
        fields =["name_street","number_street","city","commune"]