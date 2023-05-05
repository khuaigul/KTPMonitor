from django.shortcuts import render, redirect
from django.contrib.auth import login as enter_acc, logout as exit_acc
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.models import Permission
from django.http import JsonResponse
from .server import contest
from .server import div
from .server import people
from django.views.decorators.csrf import csrf_exempt
from . import tokens
from django.utils.encoding import force_str
from .models import *
from .server.DB.main_DB_modul import *
from .server.sendProfileData import send_profile_data
from .server.signin import sign_in
from .server.registrationRe import registration_Re
from .server.currentProfileData import current_profile_data

def main(request):     
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
        return JsonResponse(sign_in(request))
    return JsonResponse({'status': False})


@csrf_exempt 
def registrationRe(request):    
    if request.method == 'POST':
        return JsonResponse(registration_Re(request))
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
    if request.method == 'POST':     
        return JsonResponse(send_profile_data(request))
    return JsonResponse({"status": False})

@csrf_exempt
def currentProfileData(request):
    if request.method == 'POST':
        return JsonResponse(current_profile_data(request))
    return JsonResponse({"status": False})


@csrf_exempt
def logout(request):
    exit_acc(request)


@csrf_exempt
def divisionsRe(request):
    if request.method == 'GET':
        print("HERE")
        print (div.write_div())
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
def teachers_by_div(request):
    if request.method == 'POST':
        for i in request.POST:
            print(i)
        return JsonResponse(people.teacher_write_div(request.POST['name']))
    return JsonResponse({"status": False})


def pupilInfo(request):
    if request.method == 'GET':
        return JsonResponse(people.profile_write(request.GET['nickname']))
    return JsonResponse({"status": False})

@csrf_exempt
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

@csrf_exempt
def newDivisionRe(request):  #
    if request.method == "POST":
        return JsonResponse(div.add_div(request.POST["name"]))
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

def testParams(request):
    if (request.method == 'POST'):
        print (request.POST["id"])

def newContest(request):
    if request.method == 'POST':
        return JsonResponse(contest.add_contest(request.POST["link"], request.POST["name"], request.POST["divison"]))
    return JsonResponse({"status": False})

def deleteDivisiont(request):
    if request.method == 'POST':
        return JsonResponse(div.remove_div(request.POST["division"]))
    return JsonResponse({"status": False})

