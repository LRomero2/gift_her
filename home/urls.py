from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home')
]

handler404 = 'home.views.error_404'
handler500 = 'home.views.error_500'
