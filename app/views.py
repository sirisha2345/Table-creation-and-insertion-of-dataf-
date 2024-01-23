from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_data(request):
    dtn=input('enter dname')
    dn=int(input('enter dno'))
    dl=input('enter location')
    DTO=Dept.objects.get_or_create(dname=dtn,dno=dn,dloc=dl)[0]
    DTO.save()
    return HttpResponse('inserted data sucessfully')
def display_data(request):
    QLDO=Dept.objects.all()
    d={'dept':QLDO}
    return render(request,'display_data.html',d)

def insert_empdata(request):
    en=input('enter employee name')
    eno=int(input('enter employee number'))
    eid=int(input('enter employee id'))
    eloc=input('enter employee location')
    ETO=Emp.objects.get_or_create(empname=en,empno=eno,empid=eid,emploc=eloc)[0]
    ETO.save()
    return HttpResponse('data inserted into emp successfully')
def display_empdata(request):
    QLEO=Emp.objects.all()
    d={'emp':QLEO}
    return render(request,'display_empdata.html',d)