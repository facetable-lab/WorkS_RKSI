from django.shortcuts import render

from .models import Vacancy
from .forms import SearchForm


def index(request):
    form = SearchForm()
    city = request.GET.get('city')
    specialization = request.GET.get('specialization')
    _filter = {}
    if city or specialization:
        if city:
            _filter['city__slug'] = city
        if specialization:
            _filter['specialization__slug'] = specialization

    vacancies_list = Vacancy.objects.filter(**_filter)

    context = {
        'vacancies_list': vacancies_list,
        'form': form
    }
    return render(request, 'search_engine/index.html', context)
