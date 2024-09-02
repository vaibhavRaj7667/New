from django.shortcuts import render,redirect
from .forms import task_form,category_form
from django.contrib import messages
from .models import task
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def home(request):
    tasks = task.objects.all()
    return render(request,"home.html",{'tasks':tasks})


def task_category(request):
    if request.method == "POST":
        form = category_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_task')  # Redirect to task creation page after saving category
    else:
        form = category_form()  # Initialize an empty form for GET requests

    return render(request, "category.html", {'form': form})


def create_task(request):
    if request.method == "POST":
        form = task_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task created successfully!')
            return redirect('create_task')

    else:
        form = task_form()

    return render(request,"create_task.html",{'form':form})

def update(request,pk):
    task_instance = get_object_or_404(task, pk=pk)

    if request.method == "POST":
        form = task_form(request.POST, instance=task_instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('home')  # Redirect to the homepage or another page
    else:
        form = task_form(instance=task_instance)  # Initialize form with existing task data

    return render(request, "update.html", {'form': form})



