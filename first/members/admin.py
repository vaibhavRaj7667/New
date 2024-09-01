from django.contrib import admin
from .models import task,Category

# Register your models here.

admin.site.register(task)
admin.site.register(Category)