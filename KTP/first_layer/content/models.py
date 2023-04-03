from django.db import models
class MyModel(models.Model):
    class Meta:        
        permissions = (
            ('/menu', ''),
            ('/signin', ''),            
        )