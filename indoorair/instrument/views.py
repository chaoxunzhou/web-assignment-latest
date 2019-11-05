from django.http import HttpResponse, JsonResponse
# from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import redirect
from fondation.models import instrument


def instrument_create_page(request):
    user = request.user


    return render(request, "homepage/index.html", {})

def get_instrument_api(request):
    return JsonResponse({
        "version":"1.0"
    })

def post_instruments_create_api(request):
    name = request.POST.get("name")
    print(name)
    try:
        instrument = Instrument.object.create(
        name = name,
        user = request.user
        )

def list_page(request):


    return render(request, " instrument/list.html",{})

def get_instrument_api(request):
    instrument = Instrument.objects.filter(user=request.user)
    output = []
    for instrument in instrument.all():
        output.append({
          'id':instrument.id,
          'name':instrument.name,
          'user':instrument,user,
        })

    retrun JsonResponse({
    'instrument':instrument,
    })
