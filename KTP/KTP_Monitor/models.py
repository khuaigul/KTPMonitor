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
            ('/divisions', ''),   
            ('/div_info', ''),  
            ('/pupil', ''),   
            ('/contest', ''), 
            ('/contests', ''),
            ('/divisionStats', ''),
        )

class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    role = models.CharField(max_length=100)

class Div_Info(models.Model):
    year = models.IntegerField()
    name = models.CharField(max_length=100)
    
    @classmethod
    def get_default(cls):
        div, created = cls.objects.get_or_create(
            name='None', year = 1980) 
            # defaults=dict(description='this is not an exam'),
        # )
        return div.pk

class Pupil_Info(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    secondname = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    grade = models.IntegerField()
    CF = models.CharField(max_length=100)
    birthday = models.DateField()
    div = models.ForeignKey(Div_Info, default= Div_Info.get_default,  on_delete = models.SET_DEFAULT)
    e_mail = models.EmailField()
    phone = models.SlugField()

class Teacher_Info(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    lastname = models.CharField(max_length=100, default = 'lastname')
    firstname = models.CharField(max_length=100, default = 'firstname')
    secondname = models.CharField(max_length=100, default = 'secondname')
    CF = models.CharField(max_length=100)
    div = models.ForeignKey(Div_Info, default= Div_Info.get_default,  on_delete = models.SET_DEFAULT)
    e_mail = models.EmailField()
    phone = models.CharField(max_length=100, default = '123')

class Contest_Info(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    divs = models.ManyToManyField(Div_Info, through="Contest_Div")
       
class Contest_Div(models.Model):
    contest = models.ForeignKey(Contest_Info, on_delete=models.CASCADE)
    div = models.ForeignKey(Div_Info, on_delete=models.CASCADE)


class Task_Info(models.Model):
    letter = models.CharField(max_length=1)
    contest = models.ForeignKey(Contest_Info, on_delete = models.CASCADE)
    name =  models.CharField(max_length=100, null = True)

    
class Pupil_Task(models.Model):
    pupil =  models.ForeignKey(Pupil_Info, on_delete = models.CASCADE)
    task = models.ForeignKey(Task_Info, on_delete = models.CASCADE)
    cnt_try =  models.IntegerField(default=0)
    result = models.CharField(max_length=100, null = True)










