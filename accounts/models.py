from pyexpat import model
from django.db import models

# Create your models here.

class Customer(models.Model):
    store_name = models.CharField(max_length=200)
    contact_no = models.IntegerField()
    gst_in = models.CharField(max_length=100,blank=True,null=True)
    pan_card = models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.store_name
    class Meta:
        verbose_name_plural = 'Customer'

class Amount_Lended(models.Model):
    store_name = models.ForeignKey(Customer,on_delete=models.DO_NOTHING)
    date = models.DateField()
    amount_lended = models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return self.store_name.store_name
    class Meta:
        verbose_name_plural = 'Amount_Lended'

class Amount_Received(models.Model):
    store_name = models.ForeignKey(Customer,on_delete=models.DO_NOTHING)
    date = models.DateField()
    amount_received = models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return self.store_name.store_name
    class Meta:
        verbose_name_plural = 'Amount_Received'

class Amount_Status(models.Model):
    store_name = models.ForeignKey(Customer,on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=10,decimal_places=2,default=0,blank=True,null=True)

    @property
    def get_store_name(self):
        n = Amount_Status.objects.raw("insert into accounts_amount_status (store_name_id)select id from accounts_customer")
        return n
    @property
    def get_amount(self):
        amt = Amount_Status.objects.raw("update accounts_amount_status set amount = (select sum(amount_lended) from accounts_amount_lended where accounts_amount_lended.store_name_id = accounts_amount_status.store_name_id)- (select sum(amount_received) from accounts_amount_received where accounts_amount_received.store_name_id = accounts_amount_status.store_name_id)")
        return amt

    def save(self,*args,**kwargs):
        self.amount = self.get_amount
        self.store_name = self.get_store_name
        super(Amount_Status,self).save(*args,**kwargs)
