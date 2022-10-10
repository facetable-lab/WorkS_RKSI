from django.contrib import admin

from .models import City, Vacancy, VacancyParsed


class CityAdmin(admin.ModelAdmin):
    list_display = ('designation', 'slug')
    list_editable = ('slug',)
    list_filter = ('designation',)


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('designation', 'slug')
    list_editable = ('slug',)
    list_filter = ('designation',)


class VacancyParsedAdmin(admin.ModelAdmin):
    list_display = ('city', 'designation', 'company', 'vacancy')
    list_display_links = ('city', 'company')
    list_editable = ('vacancy',)
    list_filter = ('city', 'company', 'vacancy')


admin.site.register(City, CityAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(VacancyParsed, VacancyParsedAdmin)
