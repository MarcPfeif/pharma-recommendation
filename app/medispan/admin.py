''' admin.py '''

import csv
from django.contrib import admin
from django.db import models
from django.http import HttpResponse

# Register your models here.
from .models import Drug

''' Route of Administration

'''
class RouteOfAdminFilter(admin.SimpleListFilter):
    title = 'Route of Administration'
    parameter_name = 'route_of_administration'
    default_value = None

    def lookups(self, request, model_admin):
        pass

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(price_code=self.value())
        return queryset


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
    search_fields = ['drug_name', 'ndc_upc_hri']
    ordering = ['drug_name']
    list_display = [
        'ndc_upc_hri',
        'drug_name',
        'route_of_administration',
        'dosage_form',
        'strength',
        'strength_unit_of_measure',
        'price_code',
        'unit_price',
        'package_price'
    ]

    list_filter = (
        PriceCodeFilter,
    )

    actions = ["export_as_csv"]

    '''
        export_as_csv
        selected rows will download csv file
    '''
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

admin.site.register(Drug, DrugAdmin)
