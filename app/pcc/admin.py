from django.contrib import admin

# Register your models here.
from .models import Facility, DrugOrders

'''
    PCC Drug Orders Administration
'''
class DrugOrdersAdmin(admin.ModelAdmin):
    search_fields = ['patient_last_name']
    ordering = ['order_date']
    list_display = [
        'pcc_drug_order_id',
        'pharmacy_medication_name',
        'patient_first_name',
        'patient_last_name',
        'pharmacy_name',
        'order_date',
    ]

    #fields = DrugOrders._meta.get_fields()
    #modelFields = []
    ##for field in fields:
        ##modelFields.append(field.name)

    ##print(modelFields)
    ##readonly_fields = modelFields


admin.site.register(DrugOrders, DrugOrdersAdmin)
admin.site.register(Facility)
