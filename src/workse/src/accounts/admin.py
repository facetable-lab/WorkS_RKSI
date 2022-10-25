from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from accounts.models import Subscriber


class SubscriberCreationForm(forms.ModelForm):
    """Форма для создания новых пользователей.
    Включает все обязателье поля, плюс повторение пароля."""
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)

    class Meta:
        model = Subscriber
        fields = ('email',)

    def clean_password2(self):
        # Проверка совпадения введенных паролей.
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают!")
        return password2

    def save(self, commit=True):
        # Сохранение введенного пароля в хэшированном виде.
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class SubscriberChangeForm(forms.ModelForm):
    """Форма для обновления пользователей. Включает все поля
пользователя, но заменяет поле пароля полем
отображения хэша пароля администратора."""

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Subscriber
        fields = ('email', 'password', 'is_active', 'is_admin')

    def clean_password(self):
        # Независимо от того, что предоставляет пользователь, возвращается начальное значение.
        # Это делается здесь, а не в поле, потому,
        # что поле не имеет доступа к начальному значению.
        return self.initial['password']


class SubscriberAdmin(BaseUserAdmin):
    # Формы для добавления и изменения пользовательских экземпляров
    form = SubscriberChangeForm
    add_form = SubscriberCreationForm

    # Поля, которые будут использоваться при отображении пользовательской модели.
    # Они переопределяют определения в базовом UserAdmin
    # которые ссылаются на определенные поля в auth.User.
    list_display = ('email', 'is_admin', 'specialization', 'city', 'is_mailing')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Настройки пользователя', {'fields': ('specialization', 'city', 'is_mailing')}),
        ('Права доступа', {'fields': ('is_admin',)}),
    )

    # add_fieldsets не является стандартным атрибутом ModelAdmin. SubscriberAdmin
    # переопределяет get_fieldsets для использования этого атрибута при создании пользователя.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Регистрация SubscriberAdmin
admin.site.register(Subscriber, SubscriberAdmin)

# Ппоскольку мы не используем встроенные разрешения Django,
# отменил регистрацию групповой модели у администратора.
admin.site.unregister(Group)
