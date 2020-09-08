from django.contrib import admin
from django.urls import path
from maths.views import math, add, sub, mul, div

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', math),
    path('add/<a>/<b>', add),
    path('sub/<a>/<b>', sub),
    path('mul/<a>/<b>', mul),
    path('div/<a>/<b>', div),
]