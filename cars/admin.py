from django.contrib import admin
from cars.models import Car, Brand, Vehicle

# Register your models here.

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'type',)

admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)
