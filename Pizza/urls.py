from django.urls import path
from Pizza import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add_pizza', views.add_pizza, name="add_pizza"),
]
