from django.contrib import admin
from django.db.models import Count, Sum, ExpressionWrapper, FloatField
from django.template.response import TemplateResponse
from django.urls import path

from .models import *


class TicketAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['booking_date']
    list_display = ['name', 'booking_date']


class CarAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['number_of_seats', 'range_of_vehicle']
    list_display = ['name', 'range_of_vehicle', 'number_of_seats']


class BusroutesAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['point_of_departure', 'destination']
    list_display = ['name', 'point_of_departure', 'destination', 'pricelist']


class Ticket_detailsAdmin(admin.ModelAdmin):
    search_fields = ['Ticket']
    list_filter = ['seats', 'car', 'user']
    list_display = ['seats', 'car', 'user']


class BusAdmin(admin.ModelAdmin):
    list_filter = ['user', 'Busroutes']
    search_fields = ['id']
    list_display = ['id', 'Busroutes', 'user']


class TicketappAdminSite(admin.AdminSite):
    site_header = 'MY TICKET APP'
    site_title = 'MY TICKET APP'

    def get_urls(self):
        return [
                   path('ticket-stats/', self.stats_view) #override get url
               ] + super().get_urls()

    def stats_view(self, request):
        busroutes = Busroutes.objects.filter(active=True).count()
        stats = Busroutes.objects.annotate(busroutes_count=Count('my_bus__my_ticket')).values('id', 'name', 'busroutes_count')

        return TemplateResponse(request,
                                'admin/ticket-stats.html', {
                                    'busroutes': busroutes,
                                    'stats': stats,
                                })


admin_site = TicketappAdminSite('myadmin')

admin_site.register(User)
admin_site.register(Busroutes, BusroutesAdmin)
admin_site.register(Ticket_details, Ticket_detailsAdmin)
admin_site.register(Range_of_vehicle)
admin_site.register(Car, CarAdmin)
admin_site.register(Bus, BusAdmin)

