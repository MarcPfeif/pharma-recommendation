''' recommendation.models.py '''

from django.contrib import admin
from django.db import models

class Preferred(models.Model):
    preferred_drug_id = models.AutoField(primary_key=True)
    ndc = models.CharField(max_length=255, null=True, blank=True)
    drug_name = models.CharField(max_length=255, null=True, blank=True)
    monthly_cost = models.CharField(max_length=255, null=True, blank=True)
    preferred_priority = models.IntegerField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.drug_name

    class Meta:
        ordering = ['drug_name']
        verbose_name = 'Preferred Drug'
        verbose_name_plural = 'Preferred Drugs'

class NonPreferred(models.Model):
    non_preferred_drug_id = models.AutoField(primary_key=True)
    preferred = models.ManyToManyField(Preferred)
    ndc = models.CharField(max_length=255, null=True, blank=True)
    drug_name = models.CharField(max_length=255, null=True, blank=True)
    monthly_cost = models.CharField(max_length=255, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.drug_name

    class Meta:
        ordering = ['drug_name']
        verbose_name = 'Not Preferred Drug'
        verbose_name_plural = 'Not Preferred Drugs'
