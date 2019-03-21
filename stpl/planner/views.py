from django.shortcuts import render, get_object_or_404
from .models import Student, Classes, Schedule
from .forms import ClassForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'planner/index.html')

def getstudent (request):
    student_list=Student.objects.all()
    return render(request, 'planner/student.html', {'student_list': student_list})

def getclasses (request):
    class_list=Classes.objects.all()
    return render(request, 'planner/class.html', {'class_list': class_list})

def getclassdetail (request, id):
    classdetail=get_object_or_404(Classes, pk=id)
    return render(request, 'planner/classdetail.html', {'classdetail': classdetail})

def getschedule (request):
    schedule_list=Schedule.ojects.all()
    return render(request, 'planner/schedule.html', {'schedule_list': schedule_list})

@login_required
def newClass(request):
    form=ClassForm
    if request.method=='POST':
        form=ClassForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ClassForm()
    else:
        form=ClassForm()
    return render(request, 'planner/newclass.html', {'form': form})
    
def loginmessage(request):
    return render(request, 'planner/loginmessage.html')

def logoutmessage(request):
    return render(request, 'planner/logoutmessage.html')