from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse

menu = ['О сайте', "Добавить миньёна", "Обратная связь", "Войти"]


def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
    }
    return render(request, 'bottle/index.html', context=data)


def about(request):
    return render(request, 'bottle/about.html', {'title': 'О сайте'})


def categories(request, cat_id):
    return HttpResponse(f'<h1>Алкоголь по категориям</h1><p>id: {cat_id}</p>')


def categories_by_slug(request, cat_slug):
    return HttpResponse(f'<h1>Алкоголь по категориям</h1><p>slug: {cat_slug}</p>')


def archive(request, year):
    if year > 2024:
        url = reverse('cat', args=('alco',))
        return HttpResponsePermanentRedirect(url)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
