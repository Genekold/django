from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from .models import Minion, Category


class BigFilter(admin.SimpleListFilter):
    title = 'Статаус BIG'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('big', 'Есть BIG',),
            ('nobig', 'Нет BIG',),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'big':
            return queryset.filter(bigminion__isnull=False)
        if self.value() == 'nobig':
            return queryset.filter(bigminion__isnull=True)


@admin.register(Minion)
class MinionAdmin(admin.ModelAdmin):
    fields = ['id', 'name', 'photo', 'minion_photo', 'volume', 'strength', 'slug', 'price', 'cat', 'tags']
    readonly_fields = ['minion_photo']
    list_display = ('id', 'name', 'minion_photo', 'date_reg', 'volume', 'strength', 'slug', 'price', 'is_active', 'cat')
    list_display_links = ('name',)
    ordering = ['-date_reg', 'name']
    list_editable = ('is_active',)
    list_per_page = 5
    actions = ['set_photo', 'no_set_photo']
    search_fields = ['name__startswith', 'cat__name']
    list_filter = [BigFilter, 'cat__name', 'is_active']
    save_on_top = True

    @admin.display(description='Фото', ordering='description')
    def minion_photo(self, bottle: Minion):
        if bottle.photo:
            return mark_safe(f"<img src='{bottle.photo.url}' width=100>")
        return 'Без фото'

    @admin.action(description='Сделать "Есть фото"')
    def set_photo(self, request, queryset):
        count = queryset.update(is_active=Minion.StatusPhoto.YES)
        self.message_user(request, f'Изменено {count} записей.')

    @admin.action(description='Сделать "Нет фото"')
    def no_set_photo(self, request, queryset):
        count = queryset.update(is_active=Minion.StatusPhoto.NO)
        self.message_user(request, f'Изменено {count} записей.', messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    list_display_links = ('pk', 'name')
