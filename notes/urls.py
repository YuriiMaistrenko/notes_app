from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('https://yuriimaistrenko.github.io/notes_app/home', views.home, name='home'),
    path('https://yuriimaistrenko.github.io/notes_app/base/', views.base, name='base'),
]
