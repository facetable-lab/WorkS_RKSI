from django.shortcuts import render

from .models import Vacancy


def index(request):
    vacancies_list = Vacancy.objects.all()
    context = {
        'vacancies_list': vacancies_list
    }
    return render(request, 'search_engine/index.html', context)
