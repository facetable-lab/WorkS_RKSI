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
        verbose_name = 'вакансию'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.designation

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.designation))
        super().save(*args, **kwargs)
