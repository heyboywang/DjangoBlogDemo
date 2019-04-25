from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    auther = models.CharField(max_length=64)
    abstract = models.TextField()
    content = models.TextField()
    readnum = models.IntegerField(default=0)
    datetime = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    sortid = models.ForeignKey('Sort',on_delete=models.CASCADE)
    a_u = models.OneToOneField(User,on_delete=models.CASCADE)
    a_t = models.ManyToManyField(to='Tag')

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
