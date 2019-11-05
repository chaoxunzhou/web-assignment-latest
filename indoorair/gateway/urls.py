from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('register/success', views.register_success, name='register_success'),
    path('api/register', views.post_api_register, name='register_api'),
    path('login', views.login, name='login'),
    path('api/login', views.post_api_login, name='login_api'),
    path('login_success',views.login_success,name='login_success')
]
