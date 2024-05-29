from django.urls import path

from banktapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('contact', views.contact, name='contact'),
    path('new', views.new, name='new'),
    path('app', views.app, name='app'),
    path('logout', views.logout, name='logout'),
]
