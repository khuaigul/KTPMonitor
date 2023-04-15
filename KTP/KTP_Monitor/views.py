from django.conf import settings
from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login as dan_pidor, logout
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import Permission
from django.utils.encoding import force_str
from django.http import JsonResponse
from django.utils.encoding import force_str
import json
from .server import div
from .server import API_CF
from .server import people
from django.views.decorators.csrf import csrf_exempt
from django.contrib.contenttypes.models import ContentType
from . import tokens
from django.utils.encoding import force_bytes, force_str
from .models import *
from .server.DB.main_DB_modul import *

# print(list(User.objects.all()))


def main(request): 
    # request.GET['signin']
    return render(request, 'main/main.html')


def teacherProfile(request):
    return render(request, 'main/teacherProfile.html')

def contests(request):
    return render(request, 'main/contests.html')

def continue_registration(request, uid):
    return render(request, 'main/continue_registration.html', {'uid' : uid})


def div_info(request):
    return render(request, 'main/div_info.html')


def divisions(request):    
    return render(request, 'main/divisions.html')  

def contest(request):
    return render(request, 'main/contest.html')  


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


def editTeacherProfile(request):
    return render(request, 'main/editTeacherProfile.html')


@csrf_exempt 
def signin(request):  # Вернуть True, если авторизация прошла успешно
    if request.method=='POST':
        login = request.POST['login']
        password = request.POST['password']   
        print("DDDDDDD", login, password)
        user = authenticate(request, username=login, password=password) 
        if user is not None:
            dan_pidor(request, user)            
            return JsonResponse({'status': True})
        else:
            return JsonResponse({'status': False})
    return JsonResponse({'status': False})


@csrf_exempt 
def registrationRe(request):
    print('reg')
    if request.method == 'POST':
        to_email = request.POST['email']
        password = request.POST['password']        
        myuser = User.objects.create_user(to_email, to_email, password)
        myuser.is_active = False
        myuser.save()       
        current_site = get_current_site(request)         
        message = render_to_string('acc_active_email.html', {
                'user': myuser,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
                'token': tokens.account_activation_token.make_token(myuser),
            })
        print(message)
        mail_subject = 'Activate your blog account.'        
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()
        return JsonResponse({'status': True})
    return JsonResponse({"status": False})


@csrf_exempt
def profileData(request, uidb64, token):    
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and tokens.account_activation_token.check_token(user, token):
        if user.is_active == True:
            return JsonResponse({"status": False})                
        user.user_permissions.add(Permission.objects.get(codename="/sendProfileData"))        
        user.save()
        dan_pidor(request, user)
        return continue_registration(request, uid)
    return JsonResponse({"status": False})


@csrf_exempt
def sendProfileData(request):
    print("AAAAAAAAAAAA")
    if request.method == 'POST':     
        user = User.objects.get(pk=request.POST['uid'])
        if user.is_active == True:
            return JsonResponse({"status": False})
        user.is_active = True     
        user.role = request.POST['role']
        user.user_permissions.add(Permission.objects.get(codename="/signin")) 
        user.user_permissions.add(Permission.objects.get(codename="/viewProfileData"))       
        if user.role == 'pupil':
            pass
            #add_pupil(user.get_id(), request.POST['lastname'], request.POST['firstname'], request.POST['secondname'], 
            #    request.POST['nickname'], request.POST['birthdate'], request.POST['school'], request.POST['grade'], request.POST['phone'])
        else:
            user.user_permissions.add(Permission.objects.get(codename="/teacherProfile"))
            user.user_permissions.add(Permission.objects.get(codename="/editTeacherProfile"))            
            #add_teacher(user.get_id(), request.POST['lastname'], request.POST['firstname'], request.POST['secondname'], 
             #   request.POST['nickname'], request.POST['phone'])
        print(user.role)
        return JsonResponse({"status": True})
    return JsonResponse({"status": False})

@csrf_exempt
def viewProfileData(request):
    if request.method == 'GET':
        user = request.user
        if user.role == "teacher":
            return JsonResponse({"firstname": user.teacher.firstname, "secondname": user.teacher.secondname,
                "lastname": user.teacher.lastname, "nickname": user.teacher.nickname, "email": user.email, "phone": user.teacher.phone})
        else:
            return JsonResponse({"firstname": user.pupil.firstname, "secondname": user.pupil.secondname,
                "lastname": user.pupil.lastname, "nickname": user.pupil.nickname, "email": user.email, "phone": user.pupil.phone, 
                "school": user.pupil.school, "grade": user.pupil.grade, "birthdate": user.pupil.birthdate})
    else:
        return JsonResponse({"status": False})

@csrf_exempt
def studentData(request):
    if request.method == 'POST':
        return JsonResponse(people.people_write_div())
    return JsonResponse({"status": False})


@csrf_exempt
def divisionsRe(request):  #
    if request.method == 'POST':
        return JsonResponse(div.write_div())
    return JsonResponse({"status": False})


@csrf_exempt
def studentProfile(request):  #
    if request.method == 'POST':
        return JsonResponse(people.people_write_one(request.POST["nickname"]))
    return JsonResponse({"status": False})


@csrf_exempt
def сhangeDiv(request):
    if request.method == 'POST':
        return JsonResponse(div.change_people_div(request.POST))
    return JsonResponse({"status": False})


@csrf_exempt
def students_by_div(request):  #
    if request.method == 'POST':
        print(request.POST["div"])
        return JsonResponse(people.people_write_div_onle(request.POST["div"]))
    return JsonResponse({"status": False})


@csrf_exempt
def newDivisionRe(request):  #
    if request.method == "POST":
        return JsonResponse(div.add_div(request.POST["name"]))
    return JsonResponse({"status": False})


@csrf_exempt
def currentProfileData(request):  # Выводит информацию о пользователе, который сейчас авторизирован
    if request.method == "POST":
        return JsonResponse(people.info_person(request))
    return JsonResponse({"status": False})
