from django.shortcuts import render

from .models import Vacancy


def index(request):
    city = request.GET.get('city')
    specialization = request.GET.get('specialization')
    _filter = {}
    if city or specialization:
        if city:
            _filter['city__title'] = city
        if specialization:
            _filter['specialization__title'] = specialization

    vacancies_list = Vacancy.objects.filter(**_filter)

    context = {
        'vacancies_list': vacancies_list
    }
    return render(request, 'search_engine/index.html', context)
