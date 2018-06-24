from django.forms import ModelForm
from Pizza.models import Ingredients


class IngredientsForm(ModelForm):
    class Meta:
        model = Ingredients
        fields = ['name','description','image','code','price',]
