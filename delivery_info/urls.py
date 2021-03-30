from django.urls import path
from . import views

urlpatterns = [
    path('', views.delivery, name='delivery_info'),
]
