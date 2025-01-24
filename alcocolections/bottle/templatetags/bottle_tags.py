from django import template

from bottle.models import Category, TagMinion

register = template.Library()


@register.inclusion_tag('bottle/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {"cats": cats, 'cat_selected': cat_selected}


@register.inclusion_tag('bottle/list_tags.html')
def show_all_tags():
    return {"tags": TagMinion.objects.all()}
