from django.urls import path,include
from apps.menu.views import menus


app_name = 'menu'
urlpatterns = [
    path('', menus, name = "menu"),
    
    
   
]

