from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import render


def register(request):
    user = request.user
    context = {
        'user':user,

    }

    return render(request,"gateway/register.html",context)

def register_success(request):
    user = request.user
    context = {
        'user':user,

    }
    return render(request,"gateway/register_success.html",context)


def post_api_register(request):
    print(request.POST)
    # this is how we get data from user
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    username = request.POST.get("username")
    password = request.POST.get("password")
    email = request.POST.get("email")
    #this is for debugging
    print(first_name,last_name,username,email,password)

    try:
         user = User.objects.create_user(username,email,password)
         user.last_name = last_name
         user.first_name = first_name
         user.save()
         return JsonResponse({
             "was_successful":True,
             'reason':None,
         })
    except Exception as e:
        return JsonResponse({
            "was_successful":False,
            "reason":str(e),
            })


def post_api_login(request):
    print(request.POST)
    # this is how we get data from user
    username = request.POST.get("username")
    password = request.POST.get("password")
    #this is for debugging
    print(username,password)

    try:
         user = User.objects.create_user(username,password)
         user.save()
         return JsonResponse({
             "was_logged":True,
             'reason':None,
         })
    except Exception as e:
        return JsonResponse({
            "was_logged":False,
            "reason":None,
            })


def login(request):
    user = request.user
    return render(request,"gateway/login.html",{})


def login_success(request):
    user = request.user
    return render(request,"gateway/dashbord.html",{})
