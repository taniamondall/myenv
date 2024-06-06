from django.contrib import admin

from . import models

admin.site.register(models.Product)
admin.site.register(models.Supplier_List)


admin.site.register(models.Stock)

admin.site.register(models.Warehouse)
admin.site.register(models.User)
admin.site.register(models.Order)
admin.site.register(models.ReturnOrder)
admin.site.register(models.Payment)
admin.site.register(models.SalesList)