from django.contrib import admin

from .models import City, Specialization, Vacancy


class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(City, CityAdmin)
admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(Vacancy)
