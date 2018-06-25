from django.shortcuts import render
from Pizza.models import *
from Pizza.forms import *
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import redirect
# Create your views here.
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


@login_required(login_url='/auth/login')
def index(request):
	if(request.user.is_staff == True):
	    data = {}


	    template_name = 'index.html'
	    ingredient = Ingredients.objects.all()
	    data["ing"] = ingredient
	    lista_imag = []
	    data["mass"] = Mass.objects.all()

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
	else:
		pass

def welcome(request):
	template = "welcome.html"
	data = {}
	return render(request, template, data)



def add_pizza(request):
	data = {}
	template_name = 'indexs.html'

	print(request.POST["diccionario"])
	return render(request, template_name, data)

#INGREDIENTES
#Listar Ing
def list_Ingredients(request):
    template = 'list_Ingredients.html'
    data = {}
    object_list = Ingredients.objects.all().order_by('-code')

    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)

    return render(request, template, data)
#Add Ing
def add_Ingredients(request):
    data = {}
    if request.method == "POST":
        data['form'] = IngredientsForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return redirect('list_Ingredients')

    else:
        data['form'] = IngredientsForm()

    template_name = 'add_Ingredients.html'
    return render(request, template_name, data)

#Edit Ing
def edit_Ingredients(request,code_Ingredients):
    ingredients = Ingredients.objects.get(code=code_Ingredients)
    if request.method == 'GET':
        form = IngredientsForm(instance=ingredients)
    else:
        form = IngredientsForm(request.POST,instance=ingredients)
        if form.is_valid():
            form.save()
        return redirect('../list_Ingredients.html')
    return render(request,'add_Ingredients.html',{'form':form})

#Delete Ingredients
def delete_Ingredients(request,code_Ingredients):
    ingredients = Ingredients.objects.get(code=code_Ingredients)

    ingredients.delete()
    return redirect('../list_Ingredients')
    return render(request,'deleteCoach.html', {'team':team})

#Mass
#Listar Mass
def list_Mass(request):
    template = 'list_Mass.html'
    data = {}
    object_list = Mass.objects.all().order_by('-code')

    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)

    return render(request, template, data)
#Add Mass
def add_Mass(request):
    data = {}
    if request.method == "POST":
        data['form'] = MassForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return redirect('list_Mass')

    else:
        data['form'] = MassForm()

    template_name = 'add_Mass.html'
    return render(request, template_name, data)

#Edit Mass
def edit_Mass(request,code_Mass):
    mass = Mass.objects.get(code=code_Mass)
    if request.method == 'GET':
        form = MassForm(instance=mass)
    else:
        form = MassForm(request.POST,instance=mass)
        if form.is_valid():
            form.save()
        return redirect('../list_Mass.html')
    return render(request,'add_Mass.html',{'form':form})

#Delete Mass
def delete_Mass(request,code_Mass):
    mass = Mass.objects.get(code=code_Mass)

    mass.delete()
    return redirect('../list_Mass')
    return render(request,'deleteCoach.html', {'team':team})

#CLIENTE
#Listar Client
def list_Client(request):
    template = 'list_Client.html'
    data = {}
    object_list = Client.objects.all().order_by('-id')

    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)

    return render(request, template, data)
#Add Client
def add_Client(request):
    data = {}
    if request.method == "POST":
        data['form'] = ClientForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return redirect('list_Client')

    else:
        data['form'] = ClientForm()

    template_name = 'add_Client.html'
    return render(request, template_name, data)

#Edit Client
def edit_Client(request,id_Client):
    client = Client.objects.get(id=id_Client)
    if request.method == 'GET':
        form = ClientForm(instance=client)
    else:
        form = ClientForm(request.POST,instance=client)
        if form.is_valid():
            form.save()
        return redirect('../list_Client.html')
    return render(request,'add_Client.html',{'form':form})

#Delete Client
def delete_Client(request,id_Client):
    client = Client.objects.get(id=id_Client)

    client.delete()
    return redirect('../list_Client')
    return render(request,'deleteCoach.html', {'team':team})

def add_dir(request):
	template_name = "add_direction.html"
	data = {}
	if request.method == "POST":
		data['form'] = DirectionForm(request.POST, request.FILES)
		if data['form'].is_valid():

			direc = Direction(name_street = request.POST["name_street"],number_street= request.POST["number_street"],city = request.POST["city"],commune = request.POST["commune"]) 
			us = User.objects.get(username = request.user)
			clien = Client.objects.get(user = us)
			direc.clients = clien
			direc.save()
			return redirect('index')
	else:
		data['form'] = DirectionForm()

	return render(request, template_name, data)
	