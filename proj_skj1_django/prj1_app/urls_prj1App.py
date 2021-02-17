#khlee add 21/02/17
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]