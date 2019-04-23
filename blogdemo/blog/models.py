from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    auther = models.CharField(max_length=64)
    abstract = models.TextField()
    content = models.TextField()
    readnum = models.IntegerField(default=0)
    datetime = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    sortid = models.ForeignKey('Sort',on_delete=models.CASCADE)
    h = models.ManyToManyField(to='Tag')

    def __str__(self):
        return self.title

class Sort(models.Model):
    sortname = models.CharField(max_length=40)

    def __str__(self):
        return self.sortname

class Tag(models.Model):
    tagname = models.CharField(max_length=40)

    def __str__(self):
        return self.tagname

class Comment(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    website = models.CharField(max_length=40)
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    articleid = models.ForeignKey('Article',on_delete=models.CASCADE)





