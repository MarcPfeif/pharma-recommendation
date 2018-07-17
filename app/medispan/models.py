from django.contrib import admin
from django.db import models

# Create your models here.
class Drug(models.Model):
    medispan_id = models.AutoField(primary_key=True)
    ndc_upc_hri = models.CharField(max_length=25)
    rx_otc_indicator_code = models.CharField(max_length=1,null=True, blank=True)
    drug_descriptor_identifier = models.IntegerField(null=True, blank=True)
    generic_product_identifier = models.CharField(max_length=14,null=True, blank=True)
    price_code = models.CharField(max_length=1,null=True, blank=True)
    effective_date = models.DateField(null=True, blank=True)
    unit_price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    unit_price_extended = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    package_price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    awp_indicator_code = models.CharField(max_length=1, null=True, blank=True)
    transaction_code = models.CharField(max_length=1, null=True, blank=True)
    last_change_date = models.DateField(null=True, blank=True)
    drug_name = models.CharField(max_length=30, null=True, blank=True)
    route_of_administration = models.CharField(max_length=2, null=True, blank=True)
    dosage_form = models.CharField(max_length=4, null=True, blank=True)
    strength = models.CharField(max_length=15, null=True, blank=True)
    strength_unit_of_measure = models.CharField(max_length=10, null=True, blank=True)
    bioequivalence_code = models.CharField(max_length=1, null=True, blank=True)

    def __str__(self):
        return self.ndc_upc_hri + " - " + self.drug_name
