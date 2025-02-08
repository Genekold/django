import uuid

from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from .forms import AddMinionForm, UploadFileForm
from .models import Minion, Category, TagMinion, UploadFiles

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить миньёна', 'url_name': 'add_minion'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}
]


def index(request):
    minions = Minion.manager.all().select_related('cat')
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'minions': minions,
        'cat_selected': 0,
    }
    return render(request, 'bottle/index.html', context=data)


# def handle_uploaded_file(f):
#     name_uuid = uuid.uuid4()
#     with open(f"uploads/{name_uuid}.jpg", "wb+") as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)
#

def about(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            fp = UploadFiles(file=form.cleaned_data['file'])
            fp.save()
    else:
        form = UploadFileForm()
    return render(request, 'bottle/about.html', {'title': 'О сайте', 'form': form, 'menu': menu})


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
    if request.method == 'POST':
        form = AddMinionForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            # try:
            #     Minion.objects.create(**form.cleaned_data)
            #     return redirect('home')
            # except:
            #     form.add_error(None, 'Ошибка')
            form.save()
            return redirect('home')
    else:
        form = AddMinionForm()
    data = {
        'menu': menu,
        'title': 'Добавление пузыречка',
        'form': form,
    }
    return render(request, 'bottle/addminion.html', context=data)


def contact(request):
    return HttpResponse('Котнакты : 8-915-949-02-14')


def login(request):
    return HttpResponse('Авторизация')


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    minions = Minion.manager.filter(cat_id=category.pk).select_related('cat')

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
    minions = tag.tags.filter(is_active=Minion.StatusPhoto.YES).select_related('cat')

    data = {
        'title': f'Тэг: {tag.tag}',
        'menu': menu,
        'minions': minions,
        'cat_selected': None,
    }

    return render(request, 'bottle/index.html', context=data)
