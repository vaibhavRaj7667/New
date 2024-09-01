from django.shortcuts import render,redirect
from .forms import task_form,category_form

# Create your views here.
def home(request):
    return render(request,"home.html")


# def task_category(request):
#     if request.method =="POST":
#         form = category_form(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = category_form()
#     return render(request,"category.html",{'form':form})

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
        if form.is_valid:
            form.save()
            return redirect('home')

    else:
        form = task_form()

    return render(request,"create_task.html",{'form':form})


