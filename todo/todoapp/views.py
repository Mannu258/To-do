from django.shortcuts import render,redirect
from . models import *
from . forms import *

# Create your views here.

def home(request):
    task = Task.objects.all()
    form = Taskform()
    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    params = {'task':task,'form':form}
    return render(request,'home.html',params)

def updatetask(request,pk):
    
    task = Task.objects.get(id=pk)
    print(task)
    form = Taskform(instance=task)
    if request.method == 'POST':
        form = Taskform(request.POST ,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'update_task.html',{'form':form})

def remove(request,pk):
    item = Task.objects.get(id=pk)
    print(item)
    if request.method == 'POST':
       item.delete()
       return redirect('/')
    params = {'item':item}
    return render(request,'delete.html',params)