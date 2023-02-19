from django.shortcuts import render
from employee.models import employee
from django.contrib import messages
def showemp(request):
    showem=employee.objects.all()
    return render(request,'index.html',{'data':showem})

def insertemp(request):
    if request.method=="POST":
        if request.POST.get('ename') and request.POST.get('email'):
            saverecord=employee()
            saverecord.ename= request.POST.get('ename')
            saverecord.email=request.POST.get('email')
            saverecord.save()
            messages.success(request,'Employee '+saverecord.ename+' is save successfully..!')
            return render(request,'insert.html')
    else:
        return render(request,'insert.html')

#  Create your views here.
