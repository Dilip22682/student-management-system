from django.shortcuts import render,redirect
from .models import student_details
from .form import Stuform 
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db.models import Q


# Create your views here.

def studentlist(request,id=None):
    data=student_details.objects.all()
    return render(request,'index.html',{'data':data})

def stdentcreate(request):
    if request.method=='POST':
        form=Stuform(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            # emailId = form.cleaned_data['emailId']
            # age = form.cleaned_data['age']
            # course = form.cleaned_data['course']
            nm = form.cleaned_data['name']
            em = form.cleaned_data['emailId']
            age = form.cleaned_data['age']
            crs = form.cleaned_data['course']
            # student_details.objects.create(name=name,emailId=emailId,age=age,course=course)
            reg=student_details(name=nm,emailId=em,age=age,course=crs)
            reg.save()
            return redirect('list')
    else:
        form=Stuform()
    return render(request,'form.html',{'form':form})

 
def updateStu(request,id):
    # stu = get_object_or_404(student_details, id=id)
    if request.method == 'POST':
        stu = student_details.objects.get(id=id)
        form = Stuform(request.POST, instance=stu)
        print("form",form)
        if form.is_valid():
            form.save()
            if id:
                messages.success(request, "Student updated successfully !!")
            else:
                messages.success(request, "Student created successfully !!")
            return redirect('list')
    else:
        stu = student_details.objects.get(id=id)
        form = Stuform(instance=stu)
    return render(request, 'update_form.html', {'form': form})

    
def deleteStu(request,id):
    stuid=student_details.objects.get(id=id)
    stuid.delete()
    return redirect('list')

def searchdata(request):
    if request.method=="POST":
        query=request.POST.get('q')
        print("query:",query)
        if query:
            students = student_details.objects.filter(
                Q(name__icontains=query) |
                Q(emailId__icontains=query) |
                Q(age__icontains=query) |
                Q(course__icontains=query)
            )
            print("student:",students)
        else:
            students = student_details.objects.all()

    return render(request, 'searchdata.html', {
        'students': students
    })