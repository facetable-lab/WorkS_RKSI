from django.contrib import admin

from .models import City, Vacancy, VacancyParsed

admin.site.register(City)
admin.site.register(Vacancy)
admin.site.register(VacancyParsed)
