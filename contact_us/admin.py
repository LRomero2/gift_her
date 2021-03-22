from django.contrib import admin
from .models import SecureMessage


class SecureMessageAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'message', 'date_contacted')
    readonly_fields = ('name', 'email', 'message', 'date_contacted')
    ordering = ('-date_contacted',)


admin.site.register(SecureMessage, SecureMessageAdmin)
