from django.conf import settings
from django.shortcuts import render, redirect
from .models import MyUser
from django.contrib.auth import authenticate, login as dan_pidor, logout as exit_acc
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
from .server import contest
from .server import div
from .server import people
from django.views.decorators.csrf import csrf_exempt
from django.contrib.contenttypes.models import ContentType
from . import tokens
from django.utils.encoding import force_bytes, force_str
from .models import *
from .server.DB.main_DB_modul import *




def main(request): 
    # request.GET['signin']
    return render(request, 'main/main.html')


def teacherProfile(request):
    return render(request, 'main/teacherProfile.html')

def pupilProfile(request):
    return render(request, 'main/pupilProfile.html')

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

def pupil(request):
    return render(request, 'main/pupil.html')

def divisionStats(request):
    return render(request, 'main/divisionStats.html')


@csrf_exempt 
def signin(request):
    if request.method=='POST':
        login = request.POST['login']
        password = request.POST['password']   
        print("DDDDDDD", login, password)
        user = authenticate(request, username=login, password=password) 
        if user is not None:
            muser = MyUser.objects.get(user=user)
            dan_pidor(request, user)            
            return JsonResponse({'status': True, 'role': muser.role})
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
        muser = MyUser.objects.create(user=myuser)
        myuser.is_active = False
        muser.save()
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
        myUser = MyUser.objects.get(user=user)          
        myUser.role = request.POST['role'] 
        myUser.save()     
        myUser = MyUser.objects.get(user=user) 
        print(myUser.role)
        user.user_permissions.add(Permission.objects.get(codename="/signin")) 
        user.user_permissions.add(Permission.objects.get(codename="/viewProfileData"))
        print(request.POST['surname'])       
        if myUser.role == 'pupil':     
            user.user_permissions.add(Permission.objects.get(codename="/pupilProfile"))                   
            add_new_pupil(user, request.POST['surname'], request.POST['firstname'], request.POST['secondname'], 
                request.POST['nickname'], request.POST['datebirth'], request.POST['school'], request.POST['grade'], request.POST['phone'])
        else:
            print(request.POST['firstname'])
            user.user_permissions.add(Permission.objects.get(codename="/teacherProfile"))
            user.user_permissions.add(Permission.objects.get(codename="/editTeacherProfile"))            
            user.user_permissions.add(Permission.objects.get(codename="/divisions"))   
            user.user_permissions.add(Permission.objects.get(codename="/div_info")) 
            user.user_permissions.add(Permission.objects.get(codename="/pupil"))                     
            user.user_permissions.add(Permission.objects.get(codename="/contest"))                     
            user.user_permissions.add(Permission.objects.get(codename="/contests"))                     
            user.user_permissions.add(Permission.objects.get(codename="/divisionStats"))
            add_new_teacher(user, request.POST['surname'], request.POST['firstname'], request.POST['secondname'], 
               request.POST['nickname'], request.POST['phone'])    
        user.save()            
        return JsonResponse({"status": True})
    return JsonResponse({"status": False})

@csrf_exempt
def currentProfileData(request):
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.id)
        print(user.email)
        myUser = MyUser.objects.get(user=user)
        print(myUser.role, user.id)
        if myUser.role == "teacher":
            teacher = Teacher_Info.objects.get(user=user)   
            print(teacher.firstname)     
            return JsonResponse({"firstname": teacher.firstname, "secondname": teacher.secondname,
                "surname": teacher.lastname, "nickname": teacher.CF, "email": user.email, "phone": teacher.phone, "division": "None"})
        else:
            pupil = Pupil_Info.objects.get(user=user)   
            return JsonResponse({"firstname": pupil.firstname, "secondname": pupil.secondname,
                "surname": pupil.lastname, "nickname": pupil.CF, "email": user.email, "phone": pupil.phone, 
                "school": pupil.school, "grade": pupil.grade, "datebirth": pupil.birthday, 'division': "None"})
    else:
        return JsonResponse({"status": False})


@csrf_exempt
def logout(request):
    exit_acc(request)


@csrf_exempt
def divisionsRe(request):
    if request.method == 'GET':
        return JsonResponse(div.write_div())
    return JsonResponse({"status": False})


@csrf_exempt
def newDivisionRe(request):
    if request.method == 'POST':
        return JsonResponse(div.add_div(request.POST["name"]))
    return JsonResponse({"status": False})


@csrf_exempt
def students_by_div(request):
    if request.method == 'GET':
        return JsonResponse(people.people_write_div(request.GET['name']))
    return JsonResponse({"status": False})


@csrf_exempt
def contests_by_div(request):
    if request.method == 'GET':
        return JsonResponse(people.teacher_write_div(request.GET['name']))
    return JsonResponse({"status": False})


@csrf_exempt
def teachers_by_div(request):
    if request.method == 'GET':
        return JsonResponse(people.teacher_write_div(request.GET['name']))
    return JsonResponse({"status": False})


def pupilInfo(request):
    if request.method == 'GET':
        return JsonResponse(people.profile_write(request.GET['nickname']))
    return JsonResponse({"status": False})


def deleteDivision(request):
    if request.method == 'POST':
        return JsonResponse(div.remove_div(request.POST['division']))
    return JsonResponse({"status": False})


@csrf_exempt
def сhangeDiv(request):
    if request.method == 'POST':
        return JsonResponse(div.change_people_div(request.POST["divisions"], request.POST["nickname"]))
    return JsonResponse({"status": False})


def pupilStats(request):
    if request.method == 'GET':
        return JsonResponse({"status": False})
    return JsonResponse({"status": False})


def divisionStats(request):
    if request.method == 'GET':
        return JsonResponse({"status": False})
    return JsonResponse({"status": False})


def contestStats(request):
    if request.method == 'GET':
        return JsonResponse({"status": False})
    return JsonResponse({"status": False})


def contestsList(request):
    if request.method == 'GET':
        return JsonResponse(contest.write_contest_list(request.GET["id"]))
    return JsonResponse({"status": False})

