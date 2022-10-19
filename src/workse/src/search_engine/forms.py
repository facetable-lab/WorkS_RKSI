from django import forms

from .models import City, Specialization


class SearchForm(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects.all(), to_field_name='slug', required=False,
                                  widget=forms.Select(attrs={'class': 'form-control'}),
                                  label='Город')
    specialization = forms.ModelChoiceField(queryset=Specialization.objects.all(), to_field_name='slug', required=False,
                                            widget=forms.Select(attrs={'class': 'form-control'}),
                                            label='Специальность')
