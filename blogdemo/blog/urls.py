from django.conf.urls import url
from . import views


app_name = "blog"

urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^fullwidth/$',views.fullwidth,name="fullwidth"),
    url(r'^single/(\d+)/$',views.single,name="single"),
    url(r'^sarticle/(\d+)/$',views.sortarticle,name="sarticle"),
    url(r'^tarticle/(\d+)/$',views.tagarticle,name="tarticle"),
    url(r'^marticle/(.*?)/(.*?)/$',views.montharticle,name="marticle"),
]