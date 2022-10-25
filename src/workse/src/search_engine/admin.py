from django.contrib import admin

from .models import City, Specialization, Vacancy, Error, Url


# TODO: Улучшить отображение (CityAdmin, SpecializationAdmin, VacancyAdmin, ErrorAdmin, UrlAdmin)

class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug')


class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug')


# Регистрация моделей в админку.
admin.site.register(City, CityAdmin)
admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(Vacancy)
admin.site.register(Error)
admin.site.register(Url)
