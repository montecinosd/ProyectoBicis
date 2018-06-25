from django.urls import path
from Pizza import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add_pizza', views.add_pizza, name="add_pizza"),
    #Ingredients
    path('addIngredients', views.add_Ingredients, name="add_Ingredients"),
    path('list_Ingredients', views.list_Ingredients, name="list_Ingredients"),
    path('edit_Ingredients/<int:code_Ingredients>', views.edit_Ingredients, name="edit_Ingredients"),
    path('delete_Ingredients/<int:code_Ingredients>', views.delete_Ingredients, name="delete_Ingredients"),
    #Mass
    path('addMass', views.add_Mass, name="add_Mass"),
    path('list_Mass', views.list_Mass, name="list_Mass"),
    path('edit_Mass/<str:code_Mass>', views.edit_Mass, name="edit_Mass"),
    path('delete_Mass/<str:code_Mass>', views.delete_Mass, name="delete_Mass"),
    #Clientes
    path('addClient', views.add_Client, name="add_Client"),
    path('list_Client', views.list_Client, name="list_Client"),
    path('edit_Client/<int:id_Client>', views.edit_Client, name="edit_Client"),
    path('delete_Client/<int:id_Client>', views.delete_Client, name="delete_Client"),

]
