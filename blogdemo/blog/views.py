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

def single(request,id):
    if request.method == "POST":
        name = request.POST["name"]
        eamil = request.POST["email"]
        website = request.POST["url"]
        content = request.POST["comment"]
        articleid = request.POST["articleid"]
        art = Article.objects.get(pk=int(articleid))
        comment = Comment()
        comment.username = name
        comment.website = website
        comment.email = eamil
        comment.content = content
        comment.articleid = art
        comment.save()

    articles = Article.objects.all()
    article = Article.objects.get(pk=int(id))
    article.readnum += 1
    article.save()
    comments =article.comment_set.all()

    # return HttpResponseRedirect("/single/"+str(article.id)+"/",{"article":article,'comments':comments})
    return render(request,"blogtemplates/single.html",{"article":article,'comments':comments,"articles":articles})
    # return HttpResponse("成功")