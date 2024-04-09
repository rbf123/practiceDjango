from django.urls import path
from . import views

urlpatterns = [
    path('', views.fortune_and_horoscope, name='fortune_and_horoscope'),
]
