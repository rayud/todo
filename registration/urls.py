from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Userlogin, name="login"),
    path('register/', views.register, name="register"),
     path('logout/', views.userLogout, name = "logout"),
]