from django.contrib import admin
from django.db import models
from django.http import HttpResponse

# Register your models here.
from .models import Preferred, NonPreferred, Position

admin.site.register(Preferred)
admin.site.register(NonPreferred)
