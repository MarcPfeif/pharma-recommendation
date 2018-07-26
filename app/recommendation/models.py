''' recommendation.models.py '''

from django.contrib import admin
from django.db import models

class NonPreferred(models.Model):
    non_preferred_drug_id = models.AutoField(primary_key=True)
    ndc = models.CharField(max_length=25, null=True, blank=True)
    drug_name = models.CharField(max_length=255, null=True, blank=True)
    monthly_cost = models.CharField(max_length=255, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.drug_name

    class Meta:
        verbose_name = 'Not Preferred Drug'
        verbose_name_plural = 'Not Preferred Drugs'

class Preferred(models.Model):
    preferred_drug_id = models.AutoField(primary_key=True)
    non_preferred = models.ForeignKey(NonPreferred, on_delete=models.CASCADE)
    ndc = models.CharField(max_length=25, null=True, blank=True)
    drug_name = models.CharField(max_length=255, null=True, blank=True)
    monthly_cost = models.CharField(max_length=255, null=True, blank=True)
    preferred_priority = models.IntegerField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.drug_name

    class Meta:
        verbose_name = 'Preferred Drug'
        verbose_name_plural = 'Preferred Drugs'
