from django.contrib import admin
# Register your models here.

from .models import Customer,Amount_Lended,Amount_Received
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('store_name','contact_no','gst_in','pan_card')
    list_max_show_all = 30

admin.site.register(Customer,CustomerAdmin)

class Amount_LendedAdmin(admin.ModelAdmin):
    list_display = ('store_name','date',"amount_lended")
    list_filter = ('store_name','date')

admin.site.register(Amount_Lended,Amount_LendedAdmin)

class Amount_ReceivedAdmin(admin.ModelAdmin):
    list_display = ('store_name','date','amount_received')
    list_filter = ('store_name','date')

admin.site.register(Amount_Received,Amount_ReceivedAdmin)