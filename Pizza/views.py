from django.shortcuts import render
from Pizza.models import *
from Pizza.forms import *
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import redirect
# Create your views here.

def index(request):
    data = {}

    for i in Pizza.objects.all():
    	print(i.Ingredients.name)



    template_name = 'index.html'
    ingredient = Ingredients.objects.all()
    data["ing"] = ingredient
    lista_imag = []
    data["mass"] = Mass.objects.all()
    for i in ingredient:
    	var = " static '{}' ".format(i.image)
    	lista_imag.append(var)
    print(lista_imag)
    # data["image"]= lista_imag
    data["total"] = zip(ingredient,lista_imag)
    if request.POST:
    	lista_obj = []
    	print(request.POST["list_ing"].split(","))
    	for i in request.POST["list_ing"].split(","):
    		try:
    			lista_obj.append(Ingredients.objects.get(code=i))
    		except:
    			raise
    	masa = Mass.objects.all()
    	print(masa)
    	orden = Pizza(type_mass=masa[0])
    	for i in lista_obj:
    		orden.Ingredients.add(i)
    	print(request.POST["list_mass"])
    	return JsonResponse({})
    return render(request, template_name, data)

def add_pizza(request):
	data = {}
	template_name = 'indexs.html'
	
	print(request.POST["diccionario"])
	return render(request, template_name, data)