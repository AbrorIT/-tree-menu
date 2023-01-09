from django.db import models
from django.http import Http404
from django.urls import reverse
# Create your models here.

class Menus(models.Model):
    title = models.CharField(max_length=55)
    discriptions = models.CharField(max_length=255)
    explicit_url = models.CharField(max_length=100, blank=True, null=True)
    named_url = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"


    def save(self, *args, **kwargs):
        if self.named_url:
            named_url_parts = self.named_url.split()
            url_name = named_url_parts[0]
            params = named_url_parts[1:len(named_url_parts)]
            reversed_named_url = reverse(url_name, args=params)
            if self.explicit_url:
                if self.explicit_url != reversed_named_url:
                    raise Http404('explicit_url does not match named_url')
            else:
                self.explicit_url = reversed_named_url
        super(Menus, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def children(self):
        return self.menu_set.all()

    def get_elder_ids(self):
        if self.parent:
            return self.parent.get_elder_ids() + [self.parent.id]
        else:
            return []
