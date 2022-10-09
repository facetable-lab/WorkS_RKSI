from django.shortcuts import render

from .models import VacancyParsed


def home_view(request):
    vacancy_objects = VacancyParsed.objects.all()
    context = {
        'object_list': vacancy_objects
    }
    return render(request, 'home.html', context=context)
