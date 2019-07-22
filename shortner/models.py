from django.db import models

# Create your models here.
class tinyURL(models.Model):
    url = models.CharField(max_length=220, )
    short_code = models.CharField(max_length=20, unique=True,)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.url)