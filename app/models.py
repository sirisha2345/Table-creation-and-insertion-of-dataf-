from django.db import models

# Create your models here.
class Dept(models.Model):
    dname=models.CharField(max_length=100)
    dno=models.IntegerField()
    dloc=models.CharField(max_length=100)
class Emp(models.Model):
    empname=models.CharField(max_length=100)
    empno=models.IntegerField()
    empid=models.IntegerField()
    emploc=models.CharField(max_length=100)

