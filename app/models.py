from django.db import models

# Create your models here.

class department(models.Model):
    Deptno=models.IntegerField(primary_key=True)
    Dname=models.CharField(max_length=100)
    Loc=models.CharField(max_length=100)

    def __int__(self):
        return self.Deptno
    

class Employee(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100,unique=True)
    job=models.CharField(max_length=100)
    mgr=models.IntegerField(null=True,blank=True)
    hiredate=models.DateField()
    sal=models.IntegerField()
    comm=models.IntegerField(null=True,blank=True)
    Deptno=models.ForeignKey(department,on_delete=models.CASCADE)

    def __str__(self):
        return self.ename