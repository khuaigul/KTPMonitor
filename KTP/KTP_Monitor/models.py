from django.db import models
from django.contrib.auth.models import AbstractUser
class Permissions(models.Model):
    class Meta:        
        permissions = (
            ('/menu', ''),
            ('/signin', ''),
            ('/sendProfileData', ''),
            ('/teacherProfile', '')            
        )

class User(AbstractUser):
    role = "pupil"
    def get_id():
        return self.id


class Div_Info(models.Model):
    div_id = models.AutoField(primary_key=True)
    div_year = models.IntegerField()
    div_name = models.CharField(max_length=100)

