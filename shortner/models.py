from django.db import models
from .utils import code_generator, shortcode_creator

# Create your models here.

class tinyURL(models.Model):
    url = models.CharField(max_length=220, )
    short_code = models.CharField(max_length=20, blank=True, unique=True,)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.url)

    def save(self, *args, **kwargs):
        if self.short_code is None or self.short_code == "":
            self.short_code = shortcode_creator(self)
        super(tinyURL, self).save(*args, **kwargs)