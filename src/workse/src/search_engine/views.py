from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Vacancy
from .forms import SearchForm


# Функция отображения главной страницы сайта
def index(request):
    form = SearchForm()

    context = {
        'form': form
    }
    return render(request, 'search_engine/index.html', context)


def list_view(request):
    form = SearchForm()
    city = request.GET.get('city')
    specialization = request.GET.get('specialization')
    _filter = {}
    page_obj = []

    context = {
        'form': form,
        'city': city,
        'specialization': specialization
    }

    if city or specialization:
        if city:
            _filter['city__slug'] = city
        if specialization:
            _filter['specialization__slug'] = specialization

    vacancies_list = Vacancy.objects.filter(**_filter)

    paginator = Paginator(vacancies_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context['vacancies_list'] = page_obj

    return render(request, 'search_engine/list.html', context)
