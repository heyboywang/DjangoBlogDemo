from django.shortcuts import render
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
import datetime
import markdown

# Create your views here.

def index(request):
    articles = Article.objects.all()
    sorts = Sort.objects.all()
    tags = Tag.objects.all()
    datenow = datetime.datetime.now()
    # print(type(datenow.year))
    return render(request,"blogtemplates/index.html",{"articles":articles,"sorts":sorts,"tags":tags,"datenow":datenow})

def fullwidth(request):
    articles = Article.objects.all()
    return render(request, "blogtemplates/full-width.html",{"articles": articles})

def sortarticle(request,i):
    sorts = Sort.objects.all()
    tags = Tag.objects.all()
    datenow = datetime.datetime.now()
    sarticles = Sort.objects.get(pk=int(i)).article_set.all()
    return render(request, "blogtemplates/index.html", {"articles": sarticles, "sorts": sorts, "tags": tags,"datenow":datenow})

def tagarticle(request,i):
    sorts = Sort.objects.all()
    tags = Tag.objects.all()
    datenow = datetime.datetime.now()
    tarticles = Tag.objects.get(pk=int(i)).article_set.all()
    return render(request, "blogtemplates/index.html", {"articles": tarticles, "sorts": sorts, "tags": tags,"datenow":datenow})

def montharticle(request,y,m):
    sorts = Sort.objects.all()
    tags = Tag.objects.all()
    datenow = datetime.datetime.now()
    # print(y,type(y))
    montharticles = Article.objects.all().filter(datetime__year = y) .filter(datetime__month = m)
    # print(str(montharticles),type(montharticles))
    return render(request, "blogtemplates/index.html", {"articles": montharticles, "sorts": sorts, "tags": tags,"datenow":datenow})
    # return HttpResponse("aaaaaaa")

def single(request,id):
    if request.method == "POST":
        articleid = request.POST["articleid"]
        art = Article.objects.get(pk=int(articleid))
        comment = Comment()
        comment.username = request.POST["name"]
        comment.website = request.POST["url"]
        comment.email = request.POST["email"]
        comment.content = request.POST["comment"]
        comment.articleid = art
        comment.save()

    articles = Article.objects.all()
    sorts = Sort.objects.all()
    tags = Tag.objects.all()
    article = Article.objects.get(pk=int(id))
    article.readnum += 1
    article.save()
    comments =article.comment_set.all()

    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    article.content = md.convert(article.content)
    article.toc = md.toc


    # return HttpResponseRedirect("/single/"+str(article.id)+"/",{"article":article,'comments':comments})
    return render(request,"blogtemplates/single.html",{"article":article,'comments':comments,"articles":articles, "sorts": sorts, "tags": tags})