from multiprocessing.resource_tracker import register

from django.urls import path, register_converter
from . import views

from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('cat/<int:cat_id>/', views.categories, name='cat_id'),
    path('cat/<slug:cat_slug>/', views.categories_by_slug, name='cat'),
    path('archive/<year4:year>/', views.archive, name='archive'),
]