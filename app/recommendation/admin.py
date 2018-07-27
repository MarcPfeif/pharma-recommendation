from django.contrib import admin
from django.db import models
from django.http import HttpResponse

# Register your models here.
from .models import Preferred, NonPreferred, Position

class PreferredAdmin(models.Model):
    pass

admin.site.register(Preferred)
admin.site.register(NonPreferred)
