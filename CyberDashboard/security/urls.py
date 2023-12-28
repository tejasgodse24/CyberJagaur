from django.urls import path
from . import views

urlpatterns = [
    path('attacks-percentage', views.home, name='home'),
    path('sql', views.sql, name='sql'),
    path('phishing', views.phishing, name='phishing'),
]