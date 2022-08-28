from django.contrib import admin
from django.db import models

# Register your models here.

from .models import sale,purchase
class purchaseAdmin(admin.ModelAdmin):
    list_display = ('items','date','rate','boxes',)
    list_filter = ('items','date')
    list_max_show_all = 30

admin.site.register(purchase,purchaseAdmin)

class saleAdmin(admin.ModelAdmin):
    list_display = ('items','date','rate','boxes_out','boxes_return')
    list_filter = ('items','date')
    

admin.site.register(sale,saleAdmin)
