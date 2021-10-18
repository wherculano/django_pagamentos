from django.contrib import admin
from .models import Client, Bills


class ClientAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Client', {'fields': ['company_name', 'cnpj']}),
    ]
    list_display = ('company_name', 'cnpj')


class BillsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Info', {'fields': ['description', 'value', 'referred_company']}),
        ('Date information', {'fields': ['issue_date', 'due_date']}),
    ]
    list_display = ('description', 'value', 'referred_company', 'due_date')


admin.site.register(Client, ClientAdmin)
admin.site.register(Bills, BillsAdmin)
