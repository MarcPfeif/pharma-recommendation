''' recommendation.models.py '''

from django.contrib import admin
from django.db import models


''' Preferred Drugs '''
class Preferred(models.Model):
    preferred_drug_id = models.AutoField(primary_key=True)
    ndc = models.CharField(max_length=255, null=True, blank=True)
    drug_name = models.CharField(max_length=255, null=True, blank=True)
    monthly_cost = models.CharField(max_length=255, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    notes2 = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.drug_name

    class Meta:
        ordering = ['drug_name']
        verbose_name = 'Preferred Drug'
        verbose_name_plural = 'Preferred Drugs'

''' Non Preferred Drugs '''
class NonPreferred(models.Model):
    non_preferred_drug_id = models.AutoField(primary_key=True)
    preferred = models.ManyToManyField(Preferred, through='Position')
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

''' Preference of the Preferred Drugs '''
class Position(models.Model):
    position_id = models.AutoField(primary_key=True)
    non_preferred_drug_id = models.ForeignKey(NonPreferred, null=True, on_delete=models.SET_NULL)
    preferred_drug_id = models.ForeignKey(Preferred, null=True, on_delete=models.SET_NULL)
    position = models.IntegerField(null=True, blank=True)
