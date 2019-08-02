from django.conf import settings
from django.db import models
from .utils import code_generator, shortcode_creator
from .validators import check_com, validate_url

# Create your models here.

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

class TinyURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs = super(TinyURLManager, self).all(*args, **kwargs)
        qs_filtered = qs.filter(active=True)
        return qs_filtered

class tinyURL(models.Model):
    url = models.CharField(max_length=220, validators=[check_com, validate_url])
    short_code = models.CharField(max_length=SHORTCODE_MAX, blank=True, unique=True,)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = TinyURLManager()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.url)

    def save(self, *args, **kwargs):
        if self.short_code is None or self.short_code == "":
            self.short_code = shortcode_creator(self)
        super(tinyURL, self).save(*args, **kwargs)