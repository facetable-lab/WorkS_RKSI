from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password

Subscriber = get_user_model()


class SubscriberLoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control '
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

    def clear(self, *args, **kwargs):
        email = self.cleaned_data.get('email').strip()
        password = self.cleaned_data.get('password').strip()

        if email and password:
            subscriber_qs = Subscriber.objects.filter(email=email)
            if not subscriber_qs.exsits():
                raise forms.ValidationError('Такого пользователя нет.')
            if not check_password(password, subscriber_qs[0].password):
                raise forms.ValidationError('Неверный пароль.')

            user = authenticate(email=email, password=password)

            if not user:
                raise forms.ValidationError('Аккаунт отключен.')

        return super(SubscriberLoginForm, self).clean(*args, **kwargs)


class SubscriberRegisterForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control '
    }), label='Ваш e-mail')
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }), label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }), label='Повтор пароля')

    class Meta:
        model = Subscriber
        fields = ('email',)

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return data['password2']
