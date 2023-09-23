from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('upload/',views.upload_post,name='uploadpost'),
    path('success/',views.success,name='sucess'),

] 

