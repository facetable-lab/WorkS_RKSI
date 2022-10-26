from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from accounts.forms import SubscriberLoginForm, SubscriberRegisterForm


# TODO: Рефакторинг контекста всего файла

def login_view(request):
    form = SubscriberLoginForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        email = data.get('email')
        password = data.get('password')
        subscriber = authenticate(request, email=email, password=password)
        login(request, subscriber)
        return redirect('index')

    context = {
        'form': form
    }

    return render(request, 'accounts/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('index')


def register_view(request):
    form = SubscriberRegisterForm(request.POST or None)
    if form.is_valid():
        new_subscriber = form.save(commit=False)
        new_subscriber.set_password(form.cleaned_data['password'])
        new_subscriber.save()
        return render(request, 'accounts/register_done.html', {
            'new_subscriber': new_subscriber
        })

    context = {
        'form': form
    }

    return render(request, 'accounts/register.html', context)
