#khlee add 21/02/17
from django.urls import path
from . import views

urlpatterns = [
    path('', views.prj1App_index, name='prj1App_index'),
    path('prj1App_category1/', views.prj1App_category1, name='prj1App_category1'),
    path('prj1App_category2/', views.prj1App_category2, name='prj1App_category2'),
    path('prj1App_testLink1/', views.prj1App_testLink1, name='prj1App_testLink1'),
    path('prj1App_testLink2/', views.prj1App_testLink2, name='prj1App_testLink2'),
    path('prj1App_about/', views.prj1App_about, name='prj1App_about'),
]