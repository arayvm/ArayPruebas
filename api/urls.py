from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('load', views.load, name='Load'),
    path('procesing', views.procesing, name='Procesing')
]



