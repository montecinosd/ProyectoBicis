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
	if(request.user.is_staff == False):
	    data = {}
	    template_name = 'index.html'
	    ingredient = Ingredients.objects.all()
	    data["ing"] = ingredient
	    lista_imag = []
	    data["mass"] = Mass.objects.all()
	    data["bicicletas"] = Bicicleta.objects.all()

	    if request.POST:
	    	lista_obj = []
	    	filtro = []

	    	for i in request.POST["list_ing"].split(","):
	    		if( i != ''):
	    			filtro.append(i)
	    	for i in filtro:
	    		try:
	    			obj = Ingredients.objects.get(code=i)
	    			lista_obj.append(obj)
	    		except:
	    			raise
	    	masa = Mass.objects.get(code = request.POST["mass"])

	    	orden = Pizza(type_mass=masa)
	    	orden.save()
	    	for i in lista_obj:
	    		orden.Ingredient.add(i)

	    	price = request.POST["price"]

	    return render(request, template_name, data)
	else:
		data={}
		template_name = "index_super_user.html"
		return render(request, template_name,data)


def add_pizza(request):
    if(request.user.is_staff == True):
    	data = {}
    	template_name = 'indexs.html'

    	print(request.POST["diccionario"])
    	return render(request, template_name, data)
    else:
        return redirect('index')
#INGREDIENTES
#Listar Ing
def list_Ingredients(request):
    if(request.user.is_staff == True):

        template = 'list_Ingredients.html'
        data = {}
        object_list = Ingredients.objects.all().order_by('-pk')

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
    else:
        return redirect('index')

#Add Ing
def add_Ingredients(request):
    if(request.user.is_staff == True):

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
    else:
        return redirect('index')

#Edit Ing
def edit_Ingredients(request,pk_Ingredients):
    if(request.user.is_staff == True):

        ingredients = Ingredients.objects.get(pk=pk_Ingredients)
        if request.method == 'GET':
            form = IngredientsForm(instance=ingredients)
        else:
            form = IngredientsForm(request.POST,instance=ingredients)
            if form.is_valid():
                form.save()
            return redirect('../list_Ingredients.html')
        return render(request,'add_Ingredients.html',{'form':form})
    else:
        return redirect('index')

#Delete Ingredients
def delete_Ingredients(request,pk_Ingredients):
    if(request.user.is_staff == True):

        ingredients = Ingredients.objects.get(pk=pk_Ingredients)

        ingredients.delete()
        return redirect('../list_Ingredients')
    else:
        return redirect('index')

#Mass
#Listar Mass
def list_Mass(request):
    if(request.user.is_staff == True):

        template = 'list_Mass.html'
        data = {}
        object_list = Mass.objects.all().order_by('-pk')

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
    else:
        return redirect('index')

#Add Mass
def add_Mass(request):
    if(request.user.is_staff == True):

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
    else:
        return redirect('index')

#Edit Mass
def edit_Mass(request,pk_Mass):
    if(request.user.is_staff == True):

        mass = Mass.objects.get(pk=pk_Mass)
        if request.method == 'GET':
            form = MassForm(instance=mass)
        else:
            form = MassForm(request.POST,instance=mass)
            if form.is_valid():
                form.save()
            return redirect('list_Mass')
        return render(request,'add_Mass.html',{'form':form})
    else:
        data={}
        template_name = "index_super_user.html"
        return render(request, template_name,data)
#Delete Mass
def delete_Mass(request,pk_Mass):
    if(request.user.is_staff == True):

        mass = Mass.objects.get(pk=pk_Mass)

        mass.delete()
        return redirect('../list_Mass')
    else:
        return redirect('index')

#CLIENTE
#Listar Client
def list_Client(request):
    if(request.user.is_staff == True):

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
    else:
        return redirect('index')

#Add Client
@login_required(login_url='/auth/login')
def add_Client(request):
    if(request.user.is_staff == True):

        data = {}
        if request.method == "POST":
            data['form'] = ClientForm(request.POST, request.FILES)
            use = User.objects.all()
            users = User.objects.get(pk = len(use))

            if (data['form'].is_valid()):
                # aca el formulario valido
                us = Client(name=request.POST["name"], email=request.POST["email"],
                rut=request.POST["rut"], dv=request.POST["dv"], birthday = request.POST["birthday"])
                us.user = users
                us.save()
                return redirect('index')

        else:
            data['form'] = ClientForm()

        template_name = 'add_Client.html'
        return render(request, template_name, data)
    else:
        return redirect('index')


@login_required(login_url='/auth/login')
def add_User(request):
    if(request.user.is_staff == True):

        data = {}
        if request.method == "POST":
            data['form'] = ClientUserForm(request.POST, request.FILES)

            if (data['form'].is_valid()):
                # aca el formulario valido
                User.objects.create_user(username=request.POST["username"],
                                password= request.POST["password1"])
                return redirect('add_Client')
        else:
            data['form'] = UserCreationForm()

        template_name = 'add_Client.html'
        return render(request, template_name, data)

    else:
        return redirect('index')



#Edit Client
def edit_Client(request,id_Client):
    if(request.user.is_staff == True):

        client = Client.objects.get(id=id_Client)
        if request.method == 'GET':
            form = ClientForm(instance=client)
        else:
            form = ClientForm(request.POST,instance=client)
            if form.is_valid():
                form.save()
            return redirect('../list_Client.html')
        return render(request,'add_Client.html',{'form':form})

    else:
        return redirect('index')


#Delete Client
def delete_Client(request,id_Client):
    if(request.user.is_staff == True):

        client = Client.objects.get(id=id_Client)

        client.delete()
        return redirect('../list_Client')
    else:
        return redirect('index')


def add_dir(request):
    if(request.user.is_staff == False):

    	template_name = "add_direction.html"
    	data = {}

    	if request.method == "POST":
    		data['form'] = DirectionForm(request.POST, request.FILES)
    		if data['form'].is_valid():
    			piz = Pizza.objects.get(pk = (Pizza.objects.all().count()))
    			cost = 0
    			for i in piz.Ingredient.all():
    				cost = cost + i.price

    			cost = cost + piz.type_mass.price

    			direc = Direction(name_street = request.POST["name_street"],number_street= request.POST["number_street"],city = request.POST["city"],commune = request.POST["commune"])
    			us = User.objects.get(username = request.user)
    			clien = Client.objects.get(user = us)
    			direc.clients = clien
    			direc.save()

    			orde = Order(total_cost = cost)
    			orde.user = clien
    			orde.order_direccion = direc
    			orde.pizza = piz
    			orde.save()

    			return redirect('list_Order')


    	else:
    		data['form'] = DirectionForm()

    	return render(request, template_name, data)

    else:
        return redirect('index')

#orden
def list_Order(request):
    if(request.user.is_staff == False):

    	us = User.objects.get(username = request.user)
    	clien = Client.objects.get(user = us)
    	template = 'list_Order.html'
    	data = {}
    	object_list = Order.objects.filter(user=clien).order_by('-id')

    	paginator = Paginator(object_list, 5)
    	page = request.GET.get('page')

    	try:
    		data['object_list'] = paginator.page(page)
    	except PageNotAnInteger:
    		data['object_list'] = paginator.page(1)
    	except EmptyPage:
    		data['object_list'] = paginator.page(paginator.num_pages)

    	return render(request, template, data)

    else:
        return redirect('index')
