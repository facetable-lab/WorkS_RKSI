from django.db import DatabaseError
import codecs
import os
import sys

# Инициализация django, для работы с моделями.
project_src = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(project_src)
os.environ['DJANGO_SETTINGS_MODULE'] = 'workse.settings'

import django

django.setup()

from search_engine.models import City, Specialization, Vacancy, Error
from search_engine.parser import *

parsers = (
    (head_hunter, 'https://persianovskiy.hh.ru/search/vacancy?text=python&from=suggest_post&area=1'),
    (habr_career, 'https://career.habr.com/vacancies?locations%5B%5D=c_678&q=java&type=all')
)

city = City.objects.filter(slug='moskva').first()
specialization = Specialization.objects.filter(slug='python').first()

jobs, errors = [], []

# Запуск сбора.
for func, url in parsers:
    j, e = func(url)
    jobs += j
    errors += e

# Отчистка памяти от лишних объектов.
# TODO: refactor with if errors and delete
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
