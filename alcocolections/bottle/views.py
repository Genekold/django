import uuid

from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

from .forms import AddMinionForm, UploadFileForm
from .models import Minion, Category, TagMinion, UploadFiles
from .utils import DataMixin


class MinionHome(DataMixin, ListView):
    template_name = 'bottle/index.html'
    context_object_name = 'minions'
    title_page = 'Главная страница'
    cat_selected = 0

    def get_queryset(self):
        return Minion.manager.all().prefetch_related('cat')


def about(request):
    minion = Minion.manager.all()
    paginator = Paginator(minion, 3, orphans=2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'bottle/about.html', {'title': 'О сайте', 'page_obj': page_obj})


class ShowMinion(DataMixin, DetailView):
    template_name = 'bottle/minion.html'
    slug_url_kwarg = 'minion_slug'
    context_object_name = 'minion'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['minion'].name)

    def get_object(self, queryset=None):
        return get_object_or_404(Minion.manager, slug=self.kwargs[self.slug_url_kwarg])


class AddMinion(DataMixin, CreateView):
    form_class = AddMinionForm
    template_name = 'bottle/addminion.html'
    title_page = 'Добавление миньёна'


class UpdateMinion(DataMixin, UpdateView):
    model = Minion
    fields = ['name', 'description', 'photo', 'country', 'manufacturer', 'cat']
    template_name = 'bottle/addminion.html'
    success_url = reverse_lazy('home')
    title_page = 'Редактирование миньёна'


class DeleteMinion(DataMixin, DeleteView):
    model = Minion
    success_url = reverse_lazy('home')
    title_page = f'Удаление'


def contact(request):
    return HttpResponse('Котнакты : 8-915-949-02-14')


def login(request):
    return HttpResponse('Авторизация')


class MinionCategory(DataMixin, ListView):
    template_name = 'bottle/index.html'
    context_object_name = 'minions'
    allow_empty = False


    def get_queryset(self):
        return Minion.manager.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['minions'][0].cat
        return self.get_mixin_context(context,
                                      title='Категория - ' + cat.name,
                                      cat_selected=cat.pk
                                      )


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class MinionTags(DataMixin, ListView):
    template_name = 'bottle/index.html'
    context_object_name = 'minions'
    allow_empty = False

    def get_queryset(self):
        return Minion.manager.filter(tags__slug=self.kwargs['tag_slug']).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = TagMinion.objects.get(slug=self.kwargs['tag_slug'])
        return self.get_mixin_context(context, title='Тег - ' + tag.tag)