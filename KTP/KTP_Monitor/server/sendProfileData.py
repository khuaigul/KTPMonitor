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
    user.user_permissions.add(Permission.objects.get(codename="/signin")) 
    user.user_permissions.add(Permission.objects.get(codename="/viewProfileData"))
    print(request.POST['surname'])       
    if myUser.role == 'pupil':     
        user.user_permissions.add(Permission.objects.get(codename="/pupilProfile"))                   
        if add_new_pupil(user, request.POST['surname'], request.POST['firstname'], request.POST['secondname'], 
            request.POST['nickname'], request.POST['datebirth'], request.POST['school'], request.POST['grade'], request.POST['phone']) is False:
            return {'status': False}
    else:            
        user.user_permissions.add(Permission.objects.get(codename="/teacherProfile"))
        user.user_permissions.add(Permission.objects.get(codename="/editTeacherProfile"))            
        user.user_permissions.add(Permission.objects.get(codename="/divisions"))   
        user.user_permissions.add(Permission.objects.get(codename="/div_info")) 
        user.user_permissions.add(Permission.objects.get(codename="/pupil"))                     
        user.user_permissions.add(Permission.objects.get(codename="/contest"))                     
        user.user_permissions.add(Permission.objects.get(codename="/contests"))                     
        user.user_permissions.add(Permission.objects.get(codename="/divisionStats"))
        if add_new_teacher(user, request.POST['surname'], request.POST['firstname'], request.POST['secondname'], 
           request.POST['nickname'], request.POST['phone']) is False:
            return {'status': False}
    user.save()            
    return {"status": True}