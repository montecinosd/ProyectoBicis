from django.contrib import admin
from .models import Mass, Ingredients, Client, Pizza, Order, Direction, Bicicleta
from django.utils.safestring import mark_safe

# Register your models here.
@admin.register(Mass)
class MassAdmin(admin.ModelAdmin):
    list_display = ('name','description','image','code','price',)

@admin.register(Bicicleta)
class BicicletaAdmin(admin.ModelAdmin):
    list_display = ('nombre','modelo','color','aro','Estado','Tipo','Codigo','Imagen',)

@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('name','description','image','code','price',)

@admin.register(Client)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name','birthday','email','directions','rut',)

    def thumb(self, obj):
        return mark_safe(u'<img src="%s" style="width:10px;height:10px;"/>' \
            % (obj.picture.url))
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','total_cost','order_direccion','pizza','date')

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('type_mass',)

@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ('name_street','number_street','city','commune','clients',)
