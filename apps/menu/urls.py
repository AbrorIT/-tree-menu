from django.urls import path,include
from apps.menu.views import menus



urlpatterns = [
    path('', menus, name = "menu"),
    
   
]

