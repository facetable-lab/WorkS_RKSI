from django import forms

from .models import City, Vacancy


class SearchForm(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects.all(), to_field_name='slug', required=False,
                                  widget=forms.Select(attrs={
                                      'class': 'form-select'
                                  }), label='Город')
    specialization = forms.ModelChoiceField(queryset=Vacancy.objects.all(), to_field_name='slug', required=False,
                                            widget=forms.Select(attrs={
                                                'class': 'form-select'
                                            }), label='Специальность')
