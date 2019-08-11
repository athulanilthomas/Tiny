from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import tinyURL
from .forms import SubmitURL

# Create your views here.

class HomePage(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitURL()
        context = {
                    "title" : "Tiny Shortner",
                    "form" :  the_form,
                    "status": None,   
            }
        return render(request, 'shortener/home.html', context)
    
    def post(self, request, *args, **kwargs):
        the_form = SubmitURL(request.POST)
        context = {
            "form" :  the_form,
        }
        template = "shortener/home.html"
        if the_form.is_valid():
           new_url = the_form.cleaned_data.get("url")
           obj, created = tinyURL.objects.get_or_create(url=new_url)
           form = SubmitURL()
           if created:
            context = {
                "object": obj,
                "created": created,
                "form" :  form,
                "status":1,
            }
           else:
            context = {
                "object": obj,
                "created": created,
                "form" :  form,
                "status":2,
            }

        return render(request, template, context)

# **********************   URL will be redirected from HERE  ********************
class TinyView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(tinyURL,short_code=shortcode)
        return HttpResponseRedirect(obj.url)


#def tinyview(request, shortcode=None, *args, **kwargs):
    #try:
    #    obj_url = None
    #    qs = tinyURL.objects.filter(short_code__iexact=shortcode.upper())
    #    if qs.exists() and qs.count() == 1:
    #        obj = qs.first()
    #        obj_url = obj.url
    #    return HttpResponse("Hello {sc}".format(sc=obj_url))
    #except:
    #    pass
