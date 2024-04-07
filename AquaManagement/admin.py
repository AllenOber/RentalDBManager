# Register your models here.
from django.contrib import admin
from .models import (Customer, BCD, BCDOrderHistory, Regulator, RegulatorDetail, Wetsuit, WetsuitOrderHistory,
                     RentalOrder, RentalOrderDetail, RentalPricing, WorkOrder)

# Register your models here.
admin.site.register(Customer)
admin.site.register(BCD)
admin.site.register(BCDOrderHistory)
admin.site.register(Regulator)
admin.site.register(RegulatorDetail)
admin.site.register(Wetsuit)
admin.site.register(WetsuitOrderHistory)
admin.site.register(RentalOrder)
admin.site.register(RentalOrderDetail)
admin.site.register(RentalPricing)
admin.site.register(WorkOrder)
