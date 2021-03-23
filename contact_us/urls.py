from django.urls import path
from . import views


urlpatterns = [
    path('', views.secure_message, name='contact_us'),
    path('faq/', views.faqs, name='faqs'),
    path('about/', views.about, name='about'),
    path('thankyou/', views.thankyou_page, name='thankyou_page'),
]
