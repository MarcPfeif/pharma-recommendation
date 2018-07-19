''' admin.py '''

from django.contrib import admin
from django.db import models

# Register your models here.
from .models import Drug

class DrugAdmin(admin.ModelAdmin):
    readonly_fields = ['drug_name']
    search_fields = ['drug_name']
    ordering = ['drug_name']
    list_display = [
        'drug_name',
        'manufacturer',
        'route_of_administration',
        'dosage_form',
        'strength',
        'strength_unit_of_measure',
        'unit_price',
    ]

    def unit_price(self):
        return "$" + self.unit_price

admin.site.register(Drug, DrugAdmin)
