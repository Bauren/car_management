from django import forms
from .models import Comment, Car


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['make', 'model', 'year', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
        }
        labels = {
            'make': 'Марка автомобиля',
            'model': 'Модель автомобиля',
            'year': 'Год выпуска',
            'description': 'Описание автомобиля',
        }
