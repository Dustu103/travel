from django.urls import path , include
from . import views

urlpatterns = [
    path('check/', views.check,name ="check"),
    path('login/',views.login, name= "login"),
    path('register/',views.register, name= "register")
]