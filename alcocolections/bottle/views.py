from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from .models import Minion, Category, TagMinion

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить миньёна', 'url_name': 'add_minion'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}
]


def index(request):
    minions = Minion.manager.all()
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'minions': minions,
        'cat_selected': 0,
    }
    return render(request, 'bottle/index.html', context=data)


def about(request):
    return render(request, 'bottle/about.html', {'title': 'О сайте', 'menu': menu})


def show_minions(request, minion_slug):
    minion = get_object_or_404(Minion, slug=minion_slug)

    data = {
        'name': minion.name,
        'menu': menu,
        'minion': minion,
        'cat_selected': 1,

    }
    return render(request, 'bottle/minion.html', context=data)


def addminion(request):
    return HttpResponse('Добавление пузыречка')


def contact(request):
    return HttpResponse('Котнакты : 8-915-949-02-14')


def login(request):
    return HttpResponse('Авторизация')


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    minions = Minion.manager.filter(cat_id=category.pk)
    data = {
        'title': category.name,
        'menu': menu,
        'minions': minions,
        'cat_selected': category.pk,
    }
    return render(request, 'bottle/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_tag_minionlist(request, tag_slug):
    tag = get_object_or_404(TagMinion, slug=tag_slug)
    minions = tag.tags.filter(photo=Minion.StatusPhoto.YES)

    data = {
        'title': f'Тэг: {tag.tag}',
        'menu': menu,
        'minions': minions,
        'cat_selected': None,
    }

    return render(request, 'bottle/index.html', context=data)
