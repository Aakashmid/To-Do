from django.contrib import admin
from django.urls import path
from .import views
  
urlpatterns = [ 
    path('', views.home, name='Home') ,
    path('addTask', views.add_Task, name='Add task') ,
    path('deleteTask', views.delete_Task, name='Deleting  task') ,
    path('login', views.loginHand, name='Login') ,
    path('logout', views.logoutHand, name='Logout') ,
    path('signup', views.signUpHand, name='Sign up') ,
]
