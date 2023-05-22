from ..models import *
from .DB.main_DB_modul import *
def update_pupil_profile_data(request):
    user = User.objects.get(pk=request.user.id)
    pupil = Pupil_Info.objects.get(user=user)               
    pupil.firstname = request.POST['firstname']
    pupil.secondname = request.POST['secondname']
    pupil.lastname = request.POST['surname']
    pupil.CF = request.POST['nickname']
    pupil.phone = request.POST['phone']    
    pupil.grade = request.POST['grade']
    pupil.school = request.POST['school']
    pupil.save()
    return {'status': True}