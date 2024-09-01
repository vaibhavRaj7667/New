from django import forms
from django.forms import ModelForm
from .models import task,Category

class task_form(ModelForm):
    class  Meta:
        model = task
        fields = ['name','category','assigned_to','start_date','end_date','priority','description','location','organizer']

class category_form(ModelForm):
    class Meta:
        model = Category
        fields =['name']
