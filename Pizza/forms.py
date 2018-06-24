from django.forms import ModelForm
from Pizza.models import Ingredients, Mass, Client


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
