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


]
