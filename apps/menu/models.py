from django.db import models
from django.urls import reverse

# Create your models here.

class Menus(models.Model):
    title = models.CharField(max_length=55)
    discriptions = models.CharField(max_length=255)
    explicit_url = models.CharField(max_length=255)
    named_url = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"


    
