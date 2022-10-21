from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


# Менеджер пользователя (подписчика)
class SubscriberManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
         Создает и сохраняет пользователя (подписчика) с указанным адресом электронной почты и паролем.
        """
        if not email:
            raise ValueError('Пльзователь должен иметь электронную почту.')

        user = self.model(email=self.normalize_email(email))

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
         Создает и сохраняет суперпользователя с указанным адресом электронной почты и паролем.
        """
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


# Модель пользователя (подписчика)
class Subscriber(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email', max_length=255, unique=True)
    is_active = models.BooleanField(default=True, verbose_name='Активный аккаунт')
    is_admin = models.BooleanField(default=False, verbose_name='Администратор')
    city = models.ForeignKey('search_engine.City', on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name='Город')
    specialization = models.ForeignKey('search_engine.Specialization', on_delete=models.SET_NULL, null=True, blank=True,
                                       verbose_name='Специализация')
    is_mailing = models.BooleanField(default=True, verbose_name='Подписка на рассылку')

    objects = SubscriberManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """Есть ли у пользователя конкретное разрешение?"""
        # Простейший возможный ответ: Да, всегда
        return True

    def has_module_perms(self, app_label):
        """Есть ли у пользователя разрешения на просмотр приложения 'app_label'?"""
        # Простейший возможный ответ: Да, всегда
        return True

    @property
    def is_staff(self):
        """Является ли пользователь сотрудником?"""
        # Простейший возможный ответ: все администраторы являются сотрудниками
        return self.is_admin

    class Meta:
        verbose_name = 'подписчика'
        verbose_name_plural = 'подписчики'
