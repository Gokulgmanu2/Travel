from django.http import HttpResponse
from django.shortcuts import render
from . models import (Place)

# Create your views here.
def home(request):
    obj=Place.objects.all()
    return render(request,"index.html",{'result':obj})

# def about(request):
#     return render(request,"about.html")
#
# def contact(request):
#     return HttpResponse("contact-8075737456")
#
# def details(request):
#     return render(request,"details.html")
# def thanks(request):
#     return HttpResponse("THANK YOU FOR READING")