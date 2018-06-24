from django.urls import path
from auth_pizza import views

urlpatterns = [
    path('login', views.auth_login, name="auth_login"),
    path('loginCoach', views.auth_loginCoach, name="auth_loginCoach"),
    path('logout', views.auth_logout, name="auth_logout"),
]
