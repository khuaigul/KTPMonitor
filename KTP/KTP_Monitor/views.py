from django.shortcuts import render, redirect
from django.contrib.auth import login as enter_acc, logout as exit_acc
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.models import Permission
from django.http import JsonResponse
from .server import contest_server
from .server import div
from .server import people
from .server import stats_s
from .server import new_functions
from django.views.decorators.csrf import csrf_exempt
from . import tokens
from django.utils.encoding import force_str
from .models import *
from .server.DB.main_DB_modul import *
from .server.sendProfileData import send_profile_data
from .server.signin import sign_in
from .server.registrationRe import registration_Re
from .server.currentProfileData import current_profile_data
from .server.updateTeacherProfileData import update_teacher_profile_data


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

def division_stats(request):
    return render(request, 'main/division_stats.html')

def addContest(request):
    return render(request, 'main/addContest.html')

def edit_pupil_profile(request):
    return render(request, 'main/edit_pupil_profile.html')

def studentStatsPage(request):
    return render(request, 'main/studentStatsPage.html')

def pupilDivision(request):
    return render(request, 'main/pupilDivision.html')

def stats(request):
    return render(request, 'main/stats.html')

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
    print("SOME");
    if request.method == 'POST':
        print("HERER")
        print(current_profile_data(request))
        return JsonResponse(current_profile_data(request))
    return JsonResponse({"status": False})

@csrf_exempt
def updateTeacherProfileData(request):
    if request.method == 'POST':
        return JsonResponse(update_teacher_profile_data(request))
    return JsonResponse({'status': False})


@csrf_exempt
def logout(request):
    exit_acc(request)


@csrf_exempt
def divisionsRe(request):
    if request.method == 'GET':
        return JsonResponse(div.write_div())
    return JsonResponse({"status": False})


@csrf_exempt
def students_by_div(request):
    if request.method == 'POST':
        print(request.POST['name'])
        return JsonResponse(people.people_write_div(request.POST['name']))
    else:
        return JsonResponse({"status": False})


@csrf_exempt
def teachers_by_div(request):
    if request.method == 'POST':
        return JsonResponse(people.teacher_write_div(request.POST['name']))
    return JsonResponse({"status": False})

@csrf_exempt
def pupilInfo(request):
    if request.method == 'POST':
        return JsonResponse(people.profile_write(request.POST['nickname']))
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

@csrf_exempt
def pupilStats(request):
    if request.method == 'POST':
        return JsonResponse(stats_s.pupil_statssss(request.POST['nickname']))
    return JsonResponse({"status": False})


@csrf_exempt
def newDivisionRe(request):  #
    if request.method == "POST":
        return JsonResponse(div.add_div(request.POST["name"]))
    return JsonResponse({"status": False})


@csrf_exempt
def divisionStats(request):
    if request.method == 'GET':
        return JsonResponse(stats_s.div_stats(request.GET['division']))
    return JsonResponse({"status": False})


@csrf_exempt
def contestStats(request):
    if request.method == 'GET':
        return JsonResponse(stats_s.contest_stats(request.GET['id']))
    return JsonResponse({"status": False})


@csrf_exempt
def contestsList(request):
    if request.method == 'POST':
        return JsonResponse(contest_server.write_contest_list(request.POST["div"]))
    return JsonResponse({"status": False})


@csrf_exempt
def testParams(request):
    if (request.method == 'POST'):
        print(request.POST["id"])


@csrf_exempt
def newContest(request):
    if request.method == 'POST':
        return JsonResponse(contest_server.add_contestt(request.POST["link"], request.POST["division"]))
    return JsonResponse({"status": False})


@csrf_exempt
def deleteContest(request):
    if request.method == 'POST':
        return JsonResponse(contest_server.remove_contest(request.POST["link"]))
    return JsonResponse({"status": False})


@csrf_exempt
def updatePupilDivison(request):
    if request.method == 'POST':
        return JsonResponse(div.change_div_people(list(request.POST.items())))
    return JsonResponse({"status": False})


@csrf_exempt
def divs_with_pupil(request):
    if request.method == 'GET':
        return JsonResponse(new_functions.all_people_and_div())
    return JsonResponse({"status": False})


@csrf_exempt
def divs_with_contests(request):
    if request.method == 'GET':
        return JsonResponse(new_functions.all_contest_and_div())
    return JsonResponse({"status": False})


@csrf_exempt
def divs_full(request):
    if request.method == 'GET':
        return JsonResponse(new_functions.all_people_and_div_and_contest())
    return JsonResponse({"status": False})


@csrf_exempt
def fullStats(request):
    if request.method == 'POST':
        info = list(request.POST.items())
        pupils_info =[]
        contest_info = []
        for item in info:
            if item[0][1] == 'p':
                pupils_info.append(item[0])
            else:
                contest_info.append(item[0])
        return JsonResponse(stats_s.full_Stats(contest_info, pupils_info))
    return JsonResponse({"status": False})


