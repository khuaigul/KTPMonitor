from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .server import div
from .server import API_CF
from .server import people

@api_view(['GET', 'POST'])


def main(request):
    # request.GET['signin']
    return render(request, 'main/main.html')


def continue_registration(request):
    return render(request, 'main/continue_registration.html')


def div_info(request):
    return render(request, 'main/div_info.html')


def divisions(request):
    return render(request, 'main/divisions.html')


def menu(request):
    return render(request, 'main/menu.html')


def new_division(request):
    return render(request, 'main/new_division.html')


def registration(request):
    return render(request, 'main/registration.html')


def student_profile(request):
    return render(request, 'main/student_profile.html')


def students(request):
    return render(request, 'main/students.html')


def signin(request):
    if(request.method=='POST'):
        login = request.POST['login']
        password = request.POST['password']
        print(login, password)
# Вернуть True, если авторизация прошла успешно
    return JsonResponse({'status' : True})

