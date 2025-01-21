from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from alcocolections.bottle.models import Minion

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить миньёна', 'url_name': 'add_minion'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}
]

data_db = [
    {'id': 1, 'name': 'НОЙ Араспел 3', 'origin': 'Республика Армения', 'price': 130, 'data_of_purchase': '02.2012',
     'photo': True,
     'description': 'Коньяк обладает приятным, свежим ароматом, в котором ощущаются нотки фруктов, ванили и сладковатые шоколадные нюансы. Вкус коньяка — изысканный, фруктовый, с тонкими нюансами шоколада и оттенками сладких специй. Коньяк идеален в качестве дижестива, а также в сочетании с сухофруктами, десертами, кофе или сигарой.'},
    {'id': 2, 'name': 'НОЙ Араспел 5', 'origin': 'Республика Армения', 'price': 150, 'data_of_purchase': '03.2012',
     'photo': False},
    {'id': 3, 'name': 'Командирский', 'origin': 'Россия г. Москва', 'price': 50, 'data_of_purchase': '04.2012',
     'photo': True},
    {'id': 4, 'name': 'Старый Кенигсберг', 'origin': 'Россия г. Чернояховск', 'price': 120,
     'data_of_purchase': '05.2012', 'photo': True}
]

cats_db =[
    {'id':1, 'name': 'Коньяк'},
    {'id':2, 'name': 'Виски'},
    {'id':3, 'name': 'Водка'},
]


def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'minions': data_db,
        'cat_selected': 0,
    }
    return render(request, 'bottle/index.html', context=data)


def about(request):
    return render(request, 'bottle/about.html', {'title': 'О сайте', 'menu': menu})


def show_minions(request, minion_id):
    minion = get_object_or_404(Minion, pk=minion_id)

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


def show_category(request, cat_id):
    data = {
        'title': 'Отображение по категориям',
        'menu': menu,
        'minions': data_db,
        'cat_selected': cat_id,
    }
    return render(request, 'bottle/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
