from django.urls import path
from . import views

urlpatterns = [
    path('', views.promise_list, name='promise_list'),
]

