from django.db import models
from django.contrib.auth.models import User
class Permissions(models.Model):
    class Meta:        
        permissions = (
            ('/menu', ''),
            ('/signin', ''),
            ('/sendProfileData', ''),
            ('/teacherProfile', ''),
            ('/viewProfileData', ''),
            ('/editTeacherProfile', ''), 
            ('/pupilProfile', ''),          
        )

class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    role = models.CharField(max_length=100)

class Div_Info(models.Model):
    year = models.IntegerField()
    name = models.CharField(max_length=100)

class Pupil_Info(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    secondname = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    grade = models.IntegerField()
    CF = models.CharField(max_length=100)
    birthday = models.DateField()
    div_id = models.ForeignKey(Div_Info, null=True, on_delete = models.SET_NULL, default= None)
    e_mail = models.EmailField()
    phone = models.SlugField()

class Teacher_Info(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    lastname = models.CharField(max_length=100, default = 'ooo')
    firstname = models.CharField(max_length=100, default = 'ooo')
    secondname = models.CharField(max_length=100, default = 'ooo')
    CF = models.CharField(max_length=100)
    div_id = models.ForeignKey(Div_Info, null=True, on_delete = models.SET_NULL, default= None)
    e_mail = models.EmailField()
    phone = models.CharField(max_length=100, default = '123')
    











