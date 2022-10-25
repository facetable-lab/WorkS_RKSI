from django.db import DatabaseError
from django.contrib.auth import get_user_model
import asyncio
import codecs
import os
import sys

# Инициализация django, для работы с моделями.
project_src = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(project_src)
del project_src
os.environ['DJANGO_SETTINGS_MODULE'] = 'workse.settings'

import django

django.setup()

from search_engine.models import City, Specialization, Vacancy, Error, Url
from search_engine.parser import *

Subscriber = get_user_model()

parsers = (
    (head_hunter, 'head_hunter'),
    (habr_career, 'habr_career')
)

jobs, errors = [], []


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


# Запуск сбора в асинхронном режиме
async def run_parsers_async(value):
    func, url, city, specialization = value
    job, err = await loop.run_in_executor(None, func, url, city, specialization)
    errors.extend(err)
    jobs.extend(job)


settings = get_subscriber_settings()
url_list = get_urls(settings)

# Создание асинхронного цикла
# asyncio.get_event_loop
loop = asyncio.new_event_loop()

# Список задач для асинхронного запуска
task_list = [(func, data['url_data'][key], data['city'], data['specialization'])
             for data in url_list
             for func, key in parsers]

# Выполнение задач и предварительная отчистка памяти
del parsers, url_list  # TODO: Оптимизация отчистки памяти: City, Specialization, Subscriber, Url, Error
tasks = asyncio.wait([loop.create_task(run_parsers_async(task)) for task in task_list])

# TODO: Удалить лишние комментарии.
# Запуск сбора.
# for data in url_list:
#     for func, key in parsers:
#         url = data['url_data'][key]
#         j, e = func(url, city=data['city'], specialization=data['specialization'])
#         jobs += j
#         errors += e

loop.run_until_complete(tasks)
loop.close()

# Отчистка памяти от лишних объектов.
# TODO: refactor with if errors and delete on line 48
# del j, e, parsers
# if len(errors) == 0:
#     del errors

# Запись собранных вакансий в БД.
for job in jobs:
    vacancy = Vacancy(**job)
try:
    vacancy.save()
except DatabaseError:
    pass

if errors:
    er = Error(data=errors).save()

# file_handler = codecs.open('vacancies.txt', 'w', 'utf-8')
# file_handler.write(str(jobs))
# file_handler.close()
