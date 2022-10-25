from django.db import DatabaseError
from django.contrib.auth import get_user_model
import codecs
import os
import sys

# Инициализация django, для работы с моделями.
project_src = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(project_src)
os.environ['DJANGO_SETTINGS_MODULE'] = 'workse.settings'

import django

django.setup()

from search_engine.models import City, Specialization, Vacancy, Error, Url
from search_engine.parser import *

Subscriber = get_user_model()

parsers = (
    (head_hunter, 'https://persianovskiy.hh.ru/search/vacancy?text=python&from=suggest_post&area=1'),
    (habr_career, 'https://career.habr.com/vacancies?locations%5B%5D=c_678&q=python&type=all')
)


def get_subscriber_settings():
    settings_filtered = Subscriber.objects.filter(is_mailing=True).values()
    settings_list = set((sf['city_id'], sf['specialization_id']) for sf in settings_filtered)
    return settings_list


def get_urls(_settings):
    urls = []
    urls_qs = Url.objects.all().values()
    url_dict = {(uqs['city_id'], uqs['specialization_id']): uqs['url_data'] for uqs in urls_qs}

    for pair in _settings:
        # TODO: Переписать код компактнее
        tmp = {}
        tmp['city'] = pair[0]
        tmp['specialization'] = pair[1]
        tmp['url_data'] = url_dict[pair]
        urls.append(tmp)

    return urls


city = City.objects.filter(slug='moskva').first()
specialization = Specialization.objects.filter(slug='python').first()

jobs, errors = [], []

# Запуск сбора.
for func, url in parsers:
    j, e = func(url)
    jobs += j
    errors += e

# Отчистка памяти от лишних объектов.
# TODO: refactor with if errors and delete on line 48
del j, e, parsers
# if len(errors) == 0:
#     del errors

# Запись собранных вакансий в БД.
for job in jobs:
    vacancy = Vacancy(**job, city=city, specialization=specialization)
try:
    vacancy.save()
except DatabaseError:
    pass

if errors:
    er = Error(data=errors).save()

# file_handler = codecs.open('vacancies.txt', 'w', 'utf-8')
# file_handler.write(str(jobs))
# file_handler.close()
