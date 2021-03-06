''' pcc_orders.models.py '''

from django.contrib import admin
from django.db import models

# Create your models here.
class Facility(models.Model):
    facility_id = models.AutoField(primary_key=True)
    facility_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Facilities'
        verbose_name_plural = 'Facilities'

class DrugOrders(models.Model):
    pcc_drug_order_id = models.AutoField(primary_key=True)
    client_id = models.IntegerField(null=True, blank=True)
    phys_order_id = models.IntegerField(null=True, blank=True)
    patient_number = models.CharField(max_length=100, null=True, blank=True)
    patient_first_name = models.CharField(max_length=100, null=True, blank=True)
    patient_last_name = models.CharField(max_length=100, null=True, blank=True)
    current_census_id = models.IntegerField(null=True, blank=True)
    admission_date = models.DateField(null=True, blank=True)
    reorder = models.CharField(max_length=100, null=True, blank=True)
    order_date = models.DateTimeField(null=True, blank=True)
    MAR_start_date = models.DateTimeField(null=True, blank=True)
    MAR_end_date = models.DateTimeField(null=True, blank=True)
    order_hold_start_date = models.DateTimeField(null=True, blank=True)
    order_hold_end_date = models.DateTimeField(null=True, blank=True)
    discontinued_date = models.DateTimeField(null=True, blank=True)
    order_created_by = models.CharField(max_length=100, null=True, blank=True)
    order_created_date = models.DateTimeField(null=True, blank=True)
    order_created_by_user_long_name = models.CharField(max_length=255, null=True, blank=True)
    order_revision_by = models.CharField(max_length=100, null=True, blank=True)
    order_revision_by_date = models.DateTimeField(null=True, blank=True)
    physician_id = models.IntegerField(null=True, blank=True)
    physician_first_name = models.CharField(max_length=100, null=True, blank=True)
    physician_last_name =  models.CharField(max_length=100, null=True, blank=True)
    PRN = models.CharField(max_length=100, null=True, blank=True)
    pharmacy_name = models.CharField(max_length=100, null=True, blank=True)
    order_category_id = models.IntegerField(null=True, blank=True)
    order_category = models.CharField(max_length=100, null=True, blank=True)
    order_type_id = models.IntegerField(null=True, blank=True)
    order_type = models.CharField(max_length=100, null=True, blank=True)
    communication_method = models.CharField(max_length=100, null=True, blank=True)
    order_description = models.CharField(max_length=100, null=True, blank=True)
    related_generic = models.CharField(max_length=100, null=True, blank=True)
    advanced_directive = models.CharField(max_length=100, null=True, blank=True)
    pharmacy_medication_name = models.CharField(max_length=100, null=True, blank=True)
    strength = models.CharField(max_length=100, null=True, blank=True)
    strength_UOM = models.CharField(max_length=100, null=True, blank=True)
    form = models.CharField(max_length=100, null=True, blank=True)
    dose = models.CharField(max_length=100, null=True, blank=True)
    diet_supplement = models.CharField(max_length=100, null=True, blank=True)
    diet_type_id = models.IntegerField(null=True, blank=True)
    diet_texture = models.CharField(max_length=100, null=True, blank=True)
    fluid_consistency = models.CharField(max_length=100, null=True, blank=True)
    route_of_admin = models.CharField(max_length=100, null=True, blank=True)
    quantity_to_administer = models.CharField(max_length=100, null=True, blank=True)
    directions = models.CharField(max_length=100, null=True, blank=True)
    related_diagnoses = models.CharField(max_length=100, null=True, blank=True)
    indications_for_use = models.CharField(max_length=100, null=True, blank=True)
    nurse_admin_notes = models.CharField(max_length=100, null=True, blank=True)
    wt_vital = models.CharField(max_length=100, null=True, blank=True)
    resp_vital = models.CharField(max_length=100, null=True, blank=True)
    BPV_vital = models.CharField(max_length=100, null=True, blank=True)
    temp_vital = models.CharField(max_length=100, null=True, blank=True)
    pulse_vital = models.CharField(max_length=100, null=True, blank=True)
    BS_vital = models.CharField(max_length=100, null=True, blank=True)
    O2_vital = models.CharField(max_length=100, null=True, blank=True)
    ht_vital = models.CharField(max_length=100, null=True, blank=True)
    facility_id = models.CharField(max_length=100, null=True, blank=True)
    vitals_description = models.CharField(max_length=100, null=True, blank=True)
    value = models.CharField(max_length=100, null=True, blank=True)
    BP_vitals_description = models.CharField(max_length=255, null=True, blank=True)
    BP_value = models.CharField(max_length=100, null=True, blank=True)
    BPD_diastolic_value = models.CharField(max_length=100, null=True, blank=True)
    facility_name = models.CharField(max_length=100, null=True, blank=True)
    allergy = models.CharField(max_length=100, null=True, blank=True)
    NCSP_pho_phys_order = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Drug Orders'
        verbose_name_plural = 'Drug Orders'
