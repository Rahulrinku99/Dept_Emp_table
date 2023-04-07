from django.shortcuts import render
from app.models import *
# Create your views here.

def Dept(request):
    LOD=department.objects.all()
    d={'depts':LOD}
    return render(request,'Dept.html',d)

def Emp(request):
    LOE=Employee.objects.all()
    d={'empl':LOE}
    return render(request,'Emp.html',d)