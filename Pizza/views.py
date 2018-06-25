from django.shortcuts import render
from Pizza.models import *
from Pizza.forms import *
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import redirect
# Create your views here.

def index(request):
    data = {}


    template_name = 'index.html'
    ingredient = Ingredients.objects.all()
    data["ing"] = ingredient
    lista_imag = []
    data["mass"] = Mass.objects.all()


    data["total"] = zip(ingredient,lista_imag)
    if request.POST:
    	lista_obj = []
    	
    	for i in request.POST["list_ing"].split(","):
    		try:
    			lista_obj.append(Ingredients.objects.get(code=i))
    		except:
    			raise
    	masa = Mass.objects.get(code = request.POST["mass"])
    	
    	orden = Pizza(type_mass=masa)
    	orden.save()
    	for i in lista_obj:
    		orden.Ingredient.add(i)
    	return JsonResponse({})
    return render(request, template_name, data)

def add_pizza(request):
	data = {}
	template_name = 'indexs.html'
	
	print(request.POST["diccionario"])
	return render(request, template_name, data)