from ..models import MyUser
from ..models import *
from .DB.main_DB_modul import *
def current_profile_data(request):
    user = User.objects.get(pk=request.user.id)
    print(user.email)
    myUser = MyUser.objects.get(user=user)
    print(myUser.role, user.id)
    if myUser.role == "teacher":
        teacher = Teacher_Info.objects.get(user=user)               
        return {"firstname": teacher.firstname, "secondname": teacher.secondname,
            "surname": teacher.lastname, "nickname": teacher.CF, "email": user.email, "phone": teacher.phone, "division": teacher.div.name}
    else:
        pupil = Pupil_Info.objects.get(user=user)   
        return {"firstname": pupil.firstname, "secondname": pupil.secondname,
            "surname": pupil.lastname, "nickname": pupil.CF, "email": user.email, "phone": pupil.phone, 
            "school": pupil.school, "grade": pupil.grade, "datebirth": pupil.birthday, 'division': "None"}