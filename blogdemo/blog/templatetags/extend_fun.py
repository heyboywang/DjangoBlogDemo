from django import template
from ..models import Article

register = template.Library()


@register.filter(name='aaa')
def mylower(value):
    """
    添加转小写方法
    :param value: 应用过滤器的对象
    :return:
    """
    return value.lower()


@register.simple_tag()
def getlatestposet():
    latepost = Article.objects.all().order_by("-create_time")
    return latepost
