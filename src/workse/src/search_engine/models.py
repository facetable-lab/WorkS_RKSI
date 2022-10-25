from django.db import models


# Значение по умолчанию поля JSONField модели Url
def get_default_urls_json():
    return {'head_hunter': '',
            'habr_career': ''}


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


# Модель сохранения ошибок
class Error(models.Model):
    time_stamp = models.DateField(auto_now_add=True, verbose_name='Время')
    data = models.JSONField()

    def __str__(self):
        return str(f'{self.time_stamp} - {self.data}')


# Модель ссылок для парсера
class Url(models.Model):
    city = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name='Город')
    specialization = models.ForeignKey(Specialization, on_delete=models.PROTECT, verbose_name='Специализация')
    url_data = models.JSONField(default=get_default_urls_json)

    def __str__(self):
        return f'{self.city} | {self.specialization}'

    class Meta:
        unique_together = ('city', 'specialization')
