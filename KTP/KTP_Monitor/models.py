from django.db import models
class MyModel(models.Model):
    class Meta:        
        permissions = (
            ('/menu', ''),
            ('/signin', ''),            
        )


class Div_Info(models.Model):
    div_id = models.AutoField(primary_key=True)
    div_year = models.IntegerField()
    div_name = models.CharField(max_length=100)

