from django.shortcuts import render

from .models import VacancyParsed
from .forms import SearchForm


def home_view(request):
    search_form = SearchForm()
    searched_city = request.GET.get('city')
    searched_specialization = request.GET.get('specialization')
    filtered_vacancies = {}
    if searched_city or searched_specialization:
        if searched_city:
            filtered_vacancies['city__slug'] = searched_city
        if searched_specialization:
            filtered_vacancies['vacancy__slug'] = searched_specialization

    vacancy_objects = VacancyParsed.objects.filter(**filtered_vacancies)

    context = {
        'vacancies_list': vacancy_objects,
        'search_form': search_form
    }

    return render(request, 'search_engine/home.html', context=context)
