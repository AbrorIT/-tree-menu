from django.urls import path
from apps.menu.views import menus


urlpatterns = [
    path('<int:id>/', menus, name = "menus"),
]

