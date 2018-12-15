from django import forms

from .models import MyModel


class MyForm(forms.Form):
    class Meta:
        model = MyModel
        field = ('tahun', 'upload')
