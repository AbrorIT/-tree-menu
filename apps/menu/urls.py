from django.urls import path 
from apps.menu.views import menus



urlpatterns = [
    path('^', menus, name = "menu"),
   
]

