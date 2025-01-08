from django.http import HttpResponse, HttpResponseNotFound, Http404


def index(request):
    return HttpResponse('Cтраница приложения')

def categories(request, cat_id):
    return HttpResponse(f'<h1>Алкоголь по категориям</h1><p>id: {cat_id}</p>')

def categories_by_slug(request, cat_slug):
    return HttpResponse(f'<h1>Алкоголь по категориям</h1><p>slug: {cat_slug}</p>')

def archive(request, year):
    if year > 2023:
        raise Http404()
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')