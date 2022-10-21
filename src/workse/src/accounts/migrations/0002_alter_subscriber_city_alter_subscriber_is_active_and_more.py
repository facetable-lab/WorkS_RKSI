# Generated by Django 4.1.2 on 2022-10-21 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search_engine', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='search_engine.city', verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активный аккаунт'),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Администратор'),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='is_mailing',
            field=models.BooleanField(default=True, verbose_name='Подписка на рассылку'),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='specialization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='search_engine.specialization', verbose_name='Специализация'),
        ),
    ]
