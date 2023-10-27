from django.contrib import admin
from contact.models import *


# Register your models here.
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'subject', 'message', 'updated_date', 'created_date']
    list_editable = ['name', 'email', 'subject', 'message']

    class Meta:
        model = Message
