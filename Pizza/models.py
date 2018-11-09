from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Mass(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(upload_to='logos')
    code = models.CharField(max_length=3)
    price = models.PositiveIntegerField()
    def __str__(self):
        return self.name

class Ingredients(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(upload_to='logos')
    code = models.CharField(max_length=3)
    price = models.PositiveIntegerField()
    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=120)
    birthday = models.DateField()
    email = models.EmailField()
    directions = models.CharField(max_length=60)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    rut = models.CharField(max_length=8)
    dv = models.PositiveIntegerField()

class Direction(models.Model):
    name_street=models.CharField(max_length=120)
    number_street= models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    commune = models.CharField(max_length=120)
    clients = models.ForeignKey(Client, on_delete=models.CASCADE)

class Pizza(models.Model):
    type_mass = models.ForeignKey(Mass, on_delete=models.CASCADE)
    Ingredient = models.ManyToManyField(Ingredients)

class Order(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    total_cost =  models.PositiveIntegerField()
    order_direccion = models.ForeignKey(Direction, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

class Bicicleta(models.Model):
    nombre = models.CharField(max_length=120)
    modelo =  models.CharField(max_length=120)
    color =  models.CharField(max_length=120)
    aro =  models.CharField(max_length=120)
    Estado =  models.CharField(max_length=120)
    Tipo =  models.CharField(max_length=120)
    Codigo =  models.CharField(max_length=120)
    Monto_garantia = models.PositiveIntegerField()
    Imagen = models.ImageField(upload_to='logos')
