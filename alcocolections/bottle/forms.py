from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator

from .models import Category, BigMinion, Minion


class AddMinionForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Категория не выбрана', label='Категория')
    bigminion = forms.ModelChoiceField(queryset=BigMinion.objects.all(), required=False, empty_label='Незабродитель',
                                       label='Бродитель')

    class Meta:
        model = Minion
        fields = ['name', 'slug', 'photo', 'description', 'volume', 'strength', 'price', 'is_active', 'tags', 'cat',
                  'bigminion']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 50, 'rows': 3}),
        }
        labels = {'slug': 'URL', 'tags': 'Незнаю'}

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) > 100:
            raise ValidationError('Слишком длиный')
        return name


class UploadFileForm(forms.Form):
    file = forms.ImageField(label='Файл')



