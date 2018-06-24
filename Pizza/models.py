from django.db import models

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
    Ingredients = models.ManyToManyField(Ingredients)

class Order(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    total_cost =  models.PositiveIntegerField()
    order_direccion = models.ForeignKey(Direction, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
