
from os import link
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name="home"),
    path('ITSP220001', views.team1, name="Team1"),
    path('ITSP220002', views.team2, name="Team2"),
    path('ITSP220003', views.team3, name="Team3"),
    path('ITSP220004', views.team4, name="Team4"),
    path('ITSP220005', views.team5, name="Team5"),
    path('ITSP220006', views.team6, name="Team6"),
    path('ITSP220007', views.team7, name="Team7"),
    path('ITSP220008', views.team8, name="Team8"),
]

