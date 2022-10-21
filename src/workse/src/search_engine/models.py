from django.db import models


# Модель города
class City(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Город')
    slug = models.CharField(max_length=50, blank=True, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'


# Модель специализации
class Specialization(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Специализация')
    slug = models.CharField(max_length=50, blank=True, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'специализацию'
        verbose_name_plural = 'Специализации'


# Модель собранной вакансии
class Vacancy(models.Model):
    url = models.URLField(unique=True, verbose_name='Ссылка (url)')
    title = models.CharField(max_length=70, verbose_name='Название вакансии')
    company = models.CharField(max_length=70, verbose_name='Компания')
    description = models.TextField(verbose_name='Описание вакансии')
    city = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name='Город')
    specialization = models.ForeignKey(Specialization, on_delete=models.PROTECT, verbose_name='Специализация')
    time_stamp = models.DateField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'вакансию'
        verbose_name_plural = 'Вакансии'
