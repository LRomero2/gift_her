from django.urls import path
from . import views


urlpatterns = [
    path('', views.secure_message, name='contact'),
]