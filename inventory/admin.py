from django.contrib import admin
from inventory import models
# Register your models here.
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ['item_name','department','descriptions','is_working']
    list_filter = ['item_name','department','descriptions','is_working']
admin.site.register(models.InventoryItem, InventoryItemAdmin)