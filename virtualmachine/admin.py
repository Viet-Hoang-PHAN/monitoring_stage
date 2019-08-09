from django.contrib import admin
from .models import Site, VirtualMachine, Gateway, Terminal, Service
# Register your models here.

admin.site.index_title  = "administration"
admin.site.site_header = "Panneau d'administration Misnet"


class SiteAdmin(admin.ModelAdmin):
    list_display = ('name','adress')
    search_fields = ('name','adress')

class VMAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip')
    search_fields = ('name', 'ip')


class GatewayAdmin(admin.ModelAdmin):
    list_display = ('gateway_id', 'conf_factory', 'version')
    search_fields = ('gateway_id', 'version')

class TerminalAdmin(admin.ModelAdmin):
    list_display = ('terminal_id', 'conf_factory', 'version')
    search_fields = ('terminal_id', 'version')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_id', 'channel')
    search_fields = ('service_id', 'channel')


admin.site.register(Site, SiteAdmin)
admin.site.register(VirtualMachine, VMAdmin)
admin.site.register(Gateway, GatewayAdmin)
admin.site.register(Terminal, TerminalAdmin)
admin.site.register(Service, ServiceAdmin)
