from django.contrib import admin

# Register your models here.
from .models import Employe

class AdminEmploye(admin.ModelAdmin):
    list_display = ['eno','ename','esal','eaddres']
admin.site.register(Employe,AdminEmploye)
