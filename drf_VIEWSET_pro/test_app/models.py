from django.db import models

# Create your models here.

class Employe(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=20)
    esal=models.IntegerField()
    eaddres=models.CharField(max_length=20)