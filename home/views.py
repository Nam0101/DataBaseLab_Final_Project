from cgitb import html
from pydoc import HTMLRepr
import re
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def homePage(request):
    return render(request,'home/index.html')

def aboutPage(request):
    return render(request,'home/about.html')

