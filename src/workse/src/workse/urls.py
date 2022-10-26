from django.contrib import admin
from django.urls import path

from search_engine.views import index, list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list', list_view, name='list'),
    path('', index, name='index'),
]
