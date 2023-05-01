from django.conf import settings
from django.shortcuts import render, redirect
from ..models import MyUser
from django.contrib.auth import authenticate, login as enter_acc, logout as exit_acc
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import Permission
from django.utils.encoding import force_str
from django.utils.encoding import force_str
import json
from . import div
from . import API_CF
from . import people
from django.views.decorators.csrf import csrf_exempt
from django.contrib.contenttypes.models import ContentType
from .. import tokens
from django.utils.encoding import force_bytes, force_str
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
            "surname": teacher.lastname, "nickname": teacher.CF, "email": user.email, "phone": teacher.phone, "division": "None"}
    else:
        pupil = Pupil_Info.objects.get(user=user)   
        return {"firstname": pupil.firstname, "secondname": pupil.secondname,
            "surname": pupil.lastname, "nickname": pupil.CF, "email": user.email, "phone": pupil.phone, 
            "school": pupil.school, "grade": pupil.grade, "datebirth": pupil.birthday, 'division': "None"}