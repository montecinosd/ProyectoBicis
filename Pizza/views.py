from django.shortcuts import render
from Pizza.models import *
from Pizza.forms import *
# Create your views here.

def index(request):
    data = {}
    template_name = 'index.html'
    ingredient = Ingredients.objects.all()
    data["ing"] = ingredient

    data["mass"] = Mass.objects.all()
 

    if request.POST:
    	print(request.POST["diccionario"])
    	return JsonResponse({})
    return render(request, template_name, data)

def add_pizza(request):
	data = {}
	template_name = 'indexs.html'
	
	print(request.POST["diccionario"])
	return render(request, template_name, data)