from django.contrib import admin
from .models import BusStop, Bus, UserBusPass

# Register your models here.

class BusStopAdmin(admin.ModelAdmin):
    """Admin interface to manage coupon types."""

    list_display = ('id', 'name', 'distance_from_college')
    list_filter = ('name',)
    search_fields = ('name',)

admin.site.register(BusStop, BusStopAdmin)


class BusAdmin(admin.ModelAdmin):
    """Admin interface to manage coupon types."""

    list_display = ('id', 'bus_number', 'destination')
    list_filter = ('bus_number',)
    search_fields = ('bus_number',)

admin.site.register(Bus, BusAdmin)

admin.site.register(UserBusPass)