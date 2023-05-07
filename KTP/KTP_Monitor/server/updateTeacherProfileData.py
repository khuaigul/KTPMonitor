from ..models import *
from .DB.main_DB_modul import *
def update_teacher_profile_data(request):
    user = User.objects.get(pk=request.user.id)
    teacher = Teacher_Info.objects.get(user=user)               
    teacher.firstname = request.POST['firstname']
    teacher.secondname = request.POST['secondname']
    teacher.lastname = request.POST['surname']
    teacher.CF = request.POST['nickname']
    teacher.phone = request.POST['phone']
    teacher.div = Div_Info.objects.get(name=request.POST['division'])
    teacher.save()
    return {'status': True}