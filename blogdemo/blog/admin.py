from django.contrib import admin
from .models import *

# Register your models here.

# class ArticleAdmin(admin.ModelAdmin):


admin.site.register(Article)
admin.site.register(Sort)
admin.site.register(Tag)
admin.site.register(Comment)

