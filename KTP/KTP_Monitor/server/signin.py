from django.contrib.auth import authenticate, login as enter_acc, logout as exit_acc
from ..models import MyUser
def sign_in(request):
    login = request.POST['login']
    password = request.POST['password']        
    user = authenticate(request, username=login, password=password) 
    if user is not None:
        muser = MyUser.objects.get(user=user)
        enter_acc(request, user)            
        return {'status': True, 'role': muser.role}
    else:
        return {'status': False}