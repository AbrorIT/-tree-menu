from django.db import models

# Create your models here.
 

class Setting(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    # class Meta:
    #     verbsoe_name = "Настройка"
    #     verbsoe_name_plural = "Настройки"

