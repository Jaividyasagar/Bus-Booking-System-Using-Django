from django.contrib import admin
from .models import BusDetails
# Register your models here.

class BusDet(admin.ModelAdmin):
    # busdetextra = ['bus_no','departure']
    pass
admin.site.register(BusDetails)
