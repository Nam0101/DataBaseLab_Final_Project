from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('about/', views.aboutPage, name='aboutPage'),
]
