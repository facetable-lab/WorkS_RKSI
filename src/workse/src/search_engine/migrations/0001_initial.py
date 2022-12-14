# Generated by Django 4.1.2 on 2022-10-21 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Город')),
                ('slug', models.CharField(blank=True, max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'город',
                'verbose_name_plural': 'города',
            },
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Специализация')),
                ('slug', models.CharField(blank=True, max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'специализацию',
                'verbose_name_plural': 'Специализации',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True, verbose_name='Ссылка (url)')),
                ('title', models.CharField(max_length=70, verbose_name='Название вакансии')),
                ('company', models.CharField(max_length=70, verbose_name='Компания')),
                ('description', models.TextField(verbose_name='Описание вакансии')),
                ('time_stamp', models.DateField(auto_now_add=True, verbose_name='Дата публикации')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='search_engine.city', verbose_name='Город')),
                ('specialization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='search_engine.specialization', verbose_name='Специализация')),
            ],
            options={
                'verbose_name': 'вакансию',
                'verbose_name_plural': 'Вакансии',
            },
        ),
    ]
