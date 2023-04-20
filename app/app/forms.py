from django import forms

from .models import Smoothie


class FruitForm(forms.Form):
    category = forms.HiddenInput()

    def save(self):
        pass