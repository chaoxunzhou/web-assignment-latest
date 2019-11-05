from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('dashbord', views.dashbord, name='dashbord'),
    path('api/dashbord',views.get_dashbord_api,name="api_dashbord")
]
