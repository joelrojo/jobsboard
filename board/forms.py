from django.forms import ModelForm
from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(max_length=250)