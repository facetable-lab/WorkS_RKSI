from django.contrib import admin
from django.urls import path

from search_engine.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view),
]
