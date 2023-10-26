from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(GeneralSetting)
class GeneralSettingsAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'parameter', 'updated_date', 'created_date']
    search_fields = ['name', 'description', 'parameter']
    list_editable = ['description', 'parameter']
    class Meta:
        model = GeneralSetting
