''' recommendation.models.py '''

from django.contrib import admin
from django.db import models


''' Non Preferred Drugs '''
class NotPreferred(models.Model):
    not_preferred_drug_id = models.AutoField(primary_key=True)
    NDC = models.CharField(max_length=255, null=True, blank=True)
    not_preferred_drug_name = models.CharField(max_length=255, null=True, blank=True)
    monthly_cost = models.CharField(max_length=255, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.not_preferred_drug_name

    class Meta:
        ordering = ['not_preferred_drug_name']
        verbose_name = 'Not Preferred Drug'
        verbose_name_plural = 'Not Preferred Drugs'


''' Preferred Drugs '''
class Preferred(models.Model):
    preferred_drug_id = models.AutoField(primary_key=True)
    #preferred = models.ManyToManyField(NonPreferred, through='Position')
    not_preferred = models.ManyToManyField(NotPreferred)
    NDC = models.CharField(max_length=255, null=True, blank=True)
    preferred_drug_name = models.CharField(max_length=255, null=True, blank=True)
    monthly_cost = models.CharField(max_length=255, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.preferred_drug_name

    class Meta:
        ordering = ['preferred_drug_name']
        verbose_name = 'Preferred Drug'
        verbose_name_plural = 'Preferred Drugs'


''' Preference of the Preferred Drugs '''
class Position(models.Model):
    position_id = models.AutoField(primary_key=True)
    non_preferred_drug_id = models.ForeignKey(NotPreferred, null=True, on_delete=models.SET_NULL)
    preferred_drug_id = models.ForeignKey(Preferred, null=True, on_delete=models.SET_NULL)
    position = models.IntegerField(null=True, blank=True)
