from django.urls import path
from . import views

urlpatterns = [
    path('', 'C:\Users\User\Desktop\django\notes_app\index.html', name='index'),
    path('home/', views.home, name='home'),
    path('base/', views.base, name='base'),
]
