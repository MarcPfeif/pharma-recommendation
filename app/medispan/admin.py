''' admin.py '''

from django.contrib import admin
from django.db import models

# Register your models here.
from .models import Drug

class DrugAdmin(admin.ModelAdmin):
    readonly_fields = ['drug_name']
    search_fields = ['drug_name']
    ordering = ['drug_name']

admin.site.register(Drug, DrugAdmin)
