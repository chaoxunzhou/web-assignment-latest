from django.urls import path

from . import views

urlpatterns = [
    path('instrument/create', views.instrument_create_page, name='create_page'),
    path('instrument/update', views.instrument_update_page, name='update_page'),
    path('instrument/list', views.instrument_list_page, name='list_page'),
    path('instrument/retrieve', views.instrument_retrieve_page, name='retrieve_page'),
]
