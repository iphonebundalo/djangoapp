from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import stub

@admin.register(stub)
class Nncd.Admin(OSMGeoAdmin):
    list_display = ('tip_stuba', 'lokacija')
# Register your models here.
