from django.shortcuts import render
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
import datetime

# Create your views here.

def index(request):
    articles = Article.objects.all()
    sorts = Sort.objects.all()
    tags = Tag.objects.all()
    return render(request,"blogtemplates/index.html",{"articles":articles,"sorts":sorts,"tags":tags})