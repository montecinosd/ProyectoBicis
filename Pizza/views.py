from django.shortcuts import render
from Pizza.models import *
from Pizza.forms import *
# Create your views here.
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
def edit_Client(request,code_Client):
    Client = Client.objects.get(code=code_Client)
    if request.method == 'GET':
        form = ClientForm(instance=Client)
    else:
        form = ClientForm(request.POST,instance=Client)
        if form.is_valid():
            form.save()
        return redirect('../list_Client.html')
    return render(request,'add_Client.html',{'form':form})

#Delete Client
def delete_Client(request,code_Client):
    Client = Client.objects.get(code=code_Client)

    Client.delete()
    return redirect('../list_Client')
    return render(request,'deleteCoach.html', {'team':team})
