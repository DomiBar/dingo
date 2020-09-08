from django.contrib import admin
from django.urls import path
from greetings.views import hello, greetings

urlpatterns = [
    path('', hello),
    path('<name>', greetings),
]