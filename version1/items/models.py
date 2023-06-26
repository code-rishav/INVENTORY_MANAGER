from django.db import models

# Create your models here.
class item(models.Model):
    itemname  = models.CharField(max_length=400)
    hsn_no = models.IntegerField()
    mrp = models.DecimalField(max_digits=8,decimal_places=2)
    lending_price = models.DecimalField(max_digits=8,decimal_places=2,default=0)
    box_price = models.DecimalField(max_digits=8,decimal_places=2)
    s_gst = models.DecimalField(max_digits=5,decimal_places=2)
    c_gst = models.DecimalField(max_digits=5,decimal_places=2)
    scheme = models.DecimalField(max_digits=5,decimal_places=2)
    def __str__(self):
        return self.itemname

