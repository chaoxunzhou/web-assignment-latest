from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import render

def dashbord_page(request):
    return render(request, "dashbord/dashbord.html",{})


def get_dashbord_api(request):
    return JsonResponse({
        'avg_temperature':0,
        'avg_humidity':0,
        'avg_pressure':0,
        'avg_co2':0,
        'avg_TVOC':0,    
    })
