from django.contrib import admin

from .models import Minion

@admin.register(Minion)
class MinionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'data_purchase', 'volume', 'strength', 'price')
