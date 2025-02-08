from django.contrib import admin, messages

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
    list_display = ('name', 'photo', 'date_reg', 'volume', 'strength', 'slug', 'price', 'is_active', 'cat', 'brief_info')
    list_display_links = ('name',)
    ordering = ['-date_reg', 'name']
    list_editable = ('is_active',)
    list_per_page = 5
    actions = ['set_photo', 'no_set_photo']
    search_fields = ['name__startswith', 'cat__name']
    list_filter = [BigFilter, 'cat__name', 'is_active']
    empty_value_display = "-empty-"

    @admin.display(description='Длина', ordering='description')
    def brief_info(self, bottle: Minion):
        return f'Всего {len(bottle.name)} символов'

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
