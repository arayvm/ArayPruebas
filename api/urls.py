from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='WebHome'),
    path('api', views.api, name='api')
]



