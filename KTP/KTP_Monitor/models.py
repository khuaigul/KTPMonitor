from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import AbstractUser
class Permissions(models.Model):
    class Meta:        
        permissions = (
            ('/menu', ''),
            ('/signin', ''),
            ('/sendProfileData', ''),
            ('/teacherProfile', ''),
            ('/viewProfileData', ''),
            ('/editTeacherProfile', ''),           
        )

class User(AbstractUser):
    role = "pupil"
    def get_id():
        return self.id

=======
from django.contrib.auth.models import User
>>>>>>> 59c9759d3e419e401a1124837957127ca2d8b151

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
    name = models.CharField(max_length=100)
    CF = models.CharField(max_length=100)
    div_id = models.ForeignKey(Div_Info, null=True, on_delete = models.SET_NULL, default= None)
    e_mail = models.EmailField()
    phone_num = models.SlugField()











