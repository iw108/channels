
from django.urls import path

from . import views

app_name = 'example'

urlpatterns = [
    path('', views.index, name='index'),
    path('first-endpoint/', views.first_endpoint, name='first'),
    path('second-endpoint/', views.second_endpoint, name='second')
]
