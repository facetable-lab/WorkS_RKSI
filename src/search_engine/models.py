from django.db import models

from workse.utils import slugify


class City(models.Model):
    designation = models.CharField(max_length=50, unique=True, verbose_name='Название города')
    slug = models.CharField(max_length=50, unique=True, blank=True)

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.designation

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.designation))
        super().save(*args, **kwargs)


class Vacancy(models.Model):
    designation = models.CharField(max_length=50, unique=True, verbose_name='Вакансия')
    slug = models.CharField(max_length=50, unique=True, blank=True)

    class Meta:
        verbose_name = 'вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.designation

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.designation))
        super().save(*args, **kwargs)


class VacancyParsed(models.Model):
    url = models.URLField(unique=True, verbose_name='Ссылка')
    designation = models.CharField(max_length=250, verbose_name='Вакансия')
    company = models.CharField(max_length=250, verbose_name='Компания')
    description = models.TextField(verbose_name='Подробное описание вакансии')
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город')
    vacancy = models.ForeignKey('Vacancy', on_delete=models.SET_DEFAULT, default='Удаленная работа',
                                verbose_name='Должность')
    time_stamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'вакансия'
        verbose_name_plural = 'Собранные вакансии'

    def __str__(self):
        return self.designation
