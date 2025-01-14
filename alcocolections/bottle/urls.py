from multiprocessing.resource_tracker import register

from django.urls import path, register_converter
from . import views

from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('addminion/', views.addminion, name='add_minion'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('minion/<int:minion_id>/', views.show_minions, name='minion'),
    path('category/<int:cat_id>/', views.show_category, name='category'),
]