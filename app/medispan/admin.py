''' admin.py '''

from django.contrib import admin
from django.db import models

# Register your models here.
from .models import Drug

'''
    PriceCodeFilter
    Additional Search Filter
'''
class PriceCodeFilter(admin.SimpleListFilter):
    title = 'Price Code'
    parameter_name = 'price_code'
    default_value = None

    def lookups(self, request, model_admin):
         list_of_price_codes = []
         queryset = ['A', 'D', 'H', 'U', 'W']

         for price_code in queryset:
             list_of_price_codes.append(
                (price_code, price_code)
             )

         return list_of_price_codes

    def queryset(self, request, queryset):
        '''
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        '''
        # Compare the requested value to decide how to filter the queryset.
        if self.value():
            return queryset.filter(price_code=self.value())
        return queryset

    '''
    def value(self):
        """
        Overriding this method will allow us to always have a default value.
        """
        value = 'A'

        return value
    '''

'''
    DrugAdmin
    Drug Results
'''
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
        'price_code',
        'unit_price',
    ]

    list_filter = (
        PriceCodeFilter,
    )



admin.site.register(Drug, DrugAdmin)
