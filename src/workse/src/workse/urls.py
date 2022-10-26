from django.contrib import admin
from django.urls import path, include

from search_engine.views import index, list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', list_view, name='list'),
    path('accounts/', include(('accounts.urls', 'accounts'))),
    path('', index, name='index'),
]
