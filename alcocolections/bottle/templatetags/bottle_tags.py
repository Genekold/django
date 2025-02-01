from django import template

from bottle.models import Category, TagMinion
from django.db.models import Count

register = template.Library()


@register.inclusion_tag('bottle/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.annotate(total=Count('minions')).filter(total__gt=0)
    return {"cats": cats, 'cat_selected': cat_selected}


@register.inclusion_tag('bottle/list_tags.html')
def show_all_tags():
    return {"tags": TagMinion.objects.annotate(total=Count('tags')).filter(total__gt=0)}
