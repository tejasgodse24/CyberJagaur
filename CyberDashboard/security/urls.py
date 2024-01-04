from django.urls import path
from . import views

urlpatterns = [
    # path('attacks-percentage', views.home, name='home'),
    # path('sql', views.sql, name='sql'),
    # path('phishing', views.phishing, name='phishing'),
    path('', views.home, name='home'),
    path('dashboard/', views.index, name='dashboard'),
    path('investigation/', views.investigation, name='investigation'),
    path('prediction/', views.prediction, name='prediction'),
    path('user-awareness/', views.user_awareness, name='user_awareness'),
    path('solutions/', views.solutions, name='solutions'),
    path('json-data', views.json_data, name="json_data"),

    path('map/get-geo-cordinates/', views.get_geo_cordinates_ajax, name="get_geo_cordinates_ajax"),


    path('login/', views.login_page, name='login_page'),
    path('register/', views.register_page, name='register_page'),
    path('logout/', views.logout_page, name='logout'),


]