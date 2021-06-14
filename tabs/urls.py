from django.urls import path

from . import views

app_name = 'tabs'

urlpatterns = [
    path('', views.main_home, name='main_home'),
    path('join/', views.join_us, name='join_us'),
    path('about/', views.about_us, name='about_us'),
    path('recycle/', views.recycle, name='recycle'),
    path('consult/', views.consult, name='consult'),
]
