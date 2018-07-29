from django.contrib import admin
from django import forms
from django.db import models
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.widgets import FilteredSelectMultiple


# Register your models here.
from .models import Preferred, NotPreferred

class PreferredInline(admin.TabularInline):
    model = Preferred.not_preferred.through
    extra = 1

class PreferredAdmin(admin.ModelAdmin):
    search_fields = ['preferred_drug_name', 'NDC']
    ordering = ['preferred_drug_name']
    list_display = [
        'preferred_drug_name',
        'NDC',
        'monthly_cost'
    ]

class NotPreferredAdmin(admin.ModelAdmin):
    search_fields = ['not_preferred_drug_name', 'NDC']
    ordering = ['not_preferred_drug_name']
    list_display = [
        'not_preferred_drug_name',
        'NDC',
        'monthly_cost'
    ]
    inlines = [PreferredInline]

admin.site.register(Preferred, PreferredAdmin)
admin.site.register(NotPreferred, NotPreferredAdmin)


'''
class NonPreferredAdmin(admin.ModelAdmin):
    model = NonPreferred
    filter_horizontal = ('non_preferred',)

class NonPreferredAdminForm(forms.ModelForm):
  prefers = forms.ModelMultipleChoiceField(
    queryset=Preferred.objects.all(),
    required=False,
    widget=FilteredSelectMultiple(
      verbose_name=_('Non Preferred Admin Form'),
      is_stacked=False
    )
  )
  class Meta:
    model = Preferred
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(NonPreferredAdminForm, self).__init__(*args, **kwargs)

    if self.instance and self.instance.pk:
      self.fields['prefers'].initial = self.instance.prefers.all()

  def save(self, commit=True):
    nonPreferred = super(NonPreferredAdminForm, self).save(commit=False)

    if commit:
      nonPreferred.save()

    if nonPreferred.pk:
      nonPreferred.prefers = self.cleaned_data['prefers']
      self.save_m2m()

    return nonPreferred

class NonPreferredAdmin(admin.ModelAdmin):
  form = NonPreferredAdminForm

admin.site.register(Preferred, PreferredAdmin)
admin.site.register(NonPreferred, NonPreferredAdmin)
'''
