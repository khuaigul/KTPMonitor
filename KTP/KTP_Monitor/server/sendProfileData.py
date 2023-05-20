from ..models import MyUser
from django.contrib.auth.models import Permission
from django.views.decorators.csrf import csrf_exempt
from ..models import *
from .DB.main_DB_modul import *

def send_profile_data(request):
    user = User.objects.get(pk=request.POST['uid'])
    if user.is_active == True:
        return {"status": False}
    user.is_active = True
    myUser = MyUser.objects.get(user=user)
    myUser.role = request.POST['role']  
    myUser.save()     
    myUser = MyUser.objects.get(user=user) 
    print(myUser.role)        
    print(request.POST['surname'])       
    if myUser.role == 'pupil':     
        user.user_permissions.add(Permission.objects.get(codename='/pupilProfile'))
        user.user_permissions.add(Permission.objects.get(codename='/updatePupilProfileData'))
        user.user_permissions.add(Permission.objects.get(codename='/main'))
        user.user_permissions.add(Permission.objects.get(codename='/edit_pupil_profile'))
        user.user_permissions.add(Permission.objects.get(codename='/logout'))
        user.user_permissions.add(Permission.objects.get(codename='/signin'))
        user.user_permissions.add(Permission.objects.get(codename='/currentProfileData'))
        user.user_permissions.add(Permission.objects.get(codename='/divisionStats'))
        user.user_permissions.add(Permission.objects.get(codename='/teachers_by_div'))                   
        if add_new_pupil(user, request.POST['surname'], request.POST['firstname'], request.POST['secondname'], 
            request.POST['nickname'], request.POST['datebirth'], request.POST['school'], request.POST['grade'], request.POST['phone'], user.email) is False:
            return {'status': 'nicknameExists'}
    else:            
        user.user_permissions.add(Permission.objects.get(codename='/main'))
        user.user_permissions.add(Permission.objects.get(codename='/div_info'))
        user.user_permissions.add(Permission.objects.get(codename='/divisions'))
        user.user_permissions.add(Permission.objects.get(codename='/menu'))
        user.user_permissions.add(Permission.objects.get(codename='/new_division'))
        user.user_permissions.add(Permission.objects.get(codename='/students'))
        user.user_permissions.add(Permission.objects.get(codename='/student_profile'))
        user.user_permissions.add(Permission.objects.get(codename='/signin'))
        user.user_permissions.add(Permission.objects.get(codename='/profileData'))
        user.user_permissions.add(Permission.objects.get(codename='/divisionsRe'))
        user.user_permissions.add(Permission.objects.get(codename='/сhangeDiv'))
        user.user_permissions.add(Permission.objects.get(codename='/newDivisionRe'))
        user.user_permissions.add(Permission.objects.get(codename='/sendProfileData'))
        user.user_permissions.add(Permission.objects.get(codename='/teacherProfile'))
        user.user_permissions.add(Permission.objects.get(codename='/editTeacherProfile'))
        user.user_permissions.add(Permission.objects.get(codename='/contests'))
        user.user_permissions.add(Permission.objects.get(codename='/contest'))
        user.user_permissions.add(Permission.objects.get(codename='/currentProfileData'))
        user.user_permissions.add(Permission.objects.get(codename='/logout'))
        user.user_permissions.add(Permission.objects.get(codename='/pupil'))
        user.user_permissions.add(Permission.objects.get(codename='/students_by_div'))
        user.user_permissions.add(Permission.objects.get(codename='/teachers_by_div'))
        user.user_permissions.add(Permission.objects.get(codename='/pupilInfo'))
        user.user_permissions.add(Permission.objects.get(codename='/pupilStats'))
        user.user_permissions.add(Permission.objects.get(codename='/division_stats'))
        user.user_permissions.add(Permission.objects.get(codename='/divisionStats'))
        user.user_permissions.add(Permission.objects.get(codename='/contestStats'))
        user.user_permissions.add(Permission.objects.get(codename='/contestsList'))
        user.user_permissions.add(Permission.objects.get(codename='/deleteDivision'))
        user.user_permissions.add(Permission.objects.get(codename='/newContest'))
        user.user_permissions.add(Permission.objects.get(codename='/updateTeacherProfileData'))
        user.user_permissions.add(Permission.objects.get(codename='/addContest'))
        user.user_permissions.add(Permission.objects.get(codename='/deleteContest'))
        user.user_permissions.add(Permission.objects.get(codename='/updatePupilDivison'))
        user.user_permissions.add(Permission.objects.get(codename='/studentStatsPage'))
        user.user_permissions.add(Permission.objects.get(codename='/divs_with_pupil' ))
        user.user_permissions.add(Permission.objects.get(codename='/divs_with_contests'))
        if add_new_teacher(user, request.POST['surname'], request.POST['firstname'], request.POST['secondname'], 
           request.POST['nickname'], request.POST['phone']) is False:
            return {'status': 'nicknameExists'}
    user.save()            
    return {"status": True}