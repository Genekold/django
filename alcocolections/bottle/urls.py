from multiprocessing.resource_tracker import register

from django.urls import path, register_converter
from . import views

from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.MinionHome.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('addminion/', views.AddMinion.as_view(), name='add_minion'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('minion/<slug:minion_slug>/', views.ShowMinion.as_view(), name='minion'),
    path('category/<slug:cat_slug>/', views.MinionCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', views.MinionTags.as_view(), name='tag'),
    path('edit/<slug:slug>/', views.UpdateMinion.as_view(), name='edit'),
    path('confirm_delete/<slug:slug>/', views.DeleteMinion.as_view(), name='confirm_delete')

]
