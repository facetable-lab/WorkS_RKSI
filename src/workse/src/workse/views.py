from django.shortcuts import render

import datetime


def index(request):
    date = datetime.datetime.now()
    context = {
        'date' : date
    }
    return render(request, 'index.html', context)
