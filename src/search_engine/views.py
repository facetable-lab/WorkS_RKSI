from django.shortcuts import render

from .models import VacancyParsed


def home_view(request):
    searched_city = request.GET.get('city')
    searched_specialization = request.GET.get('specialization')
    filtered_vacancies = {}
    if searched_city or searched_specialization:
        if searched_city:
            filtered_vacancies['city__designation'] = searched_city
        if searched_specialization:
            filtered_vacancies['vacancy__designation'] = searched_specialization

    vacancy_objects = VacancyParsed.objects.filter(**filtered_vacancies)
    context = {
        'vacancies_list': vacancy_objects
    }
    return render(request, 'home.html', context=context)
