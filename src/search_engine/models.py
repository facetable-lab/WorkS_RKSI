from django.db import models


class City(models.Model):
    designation = models.CharField(max_length=50, unique=True, verbose_name='Название города')
    slug = models.CharField(max_length=50, unique=True, blank=True)

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.designation


class Vacancy(models.Model):
    designation = models.CharField(max_length=50, unique=True, verbose_name='Вакансия')
    slug = models.CharField(max_length=50, unique=True, blank=True)

    class Meta:
        verbose_name = 'вакансию'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.designation
