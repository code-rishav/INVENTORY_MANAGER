from django.contrib import admin

# Register your models here.

from .models import item
class itemsAdmin(admin.ModelAdmin):
    list_display = ('itemname','hsn_no','mrp','s_gst','c_gst','box_price','scheme')


admin.site.register(item,itemsAdmin)