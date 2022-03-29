from django.conf.urls import path, include

from . import views

urlpatterns = [
    path('', views.work, name='index')

]
