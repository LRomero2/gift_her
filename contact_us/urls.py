from django.urls import path
from . import views


urlpatterns = [
    path('', views.secure_message, name='contact_us'),
    path('contact/', views.faqs, name='faqs'),
    path('contact/', views.about, name='about'),
    path('contact/', views.thankyou_page, name='thankyou_page'),
]
