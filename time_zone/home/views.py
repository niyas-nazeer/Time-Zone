from django.shortcuts import render
from django.http import HttpResponse as hr

# Create your views here.

def display(request):
    return render(request,'home.html')