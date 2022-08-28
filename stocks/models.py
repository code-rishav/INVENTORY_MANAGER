
from operator import mod
from django.db import models
from datetime import date
from items.models import item

import psycopg2

# Create your models here.

class stock(models.Model):
    items = models.ForeignKey(item,on_delete=models.DO_NOTHING)
    box = models.IntegerField(default=0,null=True,blank=True)
    price = models.DecimalField(max_digits=8,decimal_places=2,default=0,blank=True,null=True)


    @property
    def get_items(self):
        item = sale.objects.raw("insert into stocks_stock (items_id)select id from items_item")
        return item
    @property
    def get_box(self):
        box = sale.objects.raw("update stocks_stock set box = (select sum(boxes) from stocks_purchase where stocks_stock.items_id= stocks_purchase.items_id) - (select sum(boxes_out) from stocks_sale where stocks_stock.items_id=stocks_sale.items_id) + (select sum(boxes_return) from stocks_sale where stocks_stock.items_id=stocks_sale.items_id)")
        return box
    @property
    def get_price(self):
        prc = sale.ojects.raw("update stocks_stock set price = (select items_item.lending_price from items_item where stocks_stock.items_id = items_item.id)* box")
        return prc

    def save(self,*args,**kwargs):
        self.boxes = self.get_box
        self.items = self.get_items
        self.price = self.get_price
        super(stock,self).save(*args,**kwargs)



class purchase(models.Model):
    items = models.ForeignKey(item,on_delete=models.DO_NOTHING)
    date = models.DateField()
    rate = models.DecimalField(max_digits = 7,decimal_places = 2)
    boxes = models.IntegerField()
    price = models.DecimalField(max_digits=8,decimal_places= 2,blank=True,null=True)

    def __str__(self):
        return self.items.itemname

    
    @property
    def get_price(self):
        return self.rate * self.boxes
    
    def save(self,*args,**kwargs):
        self.price = self.get_price
        super(purchase,self).save(*args,**kwargs)

    

class sale(models.Model):
    items = models.ForeignKey(item,on_delete=models.DO_NOTHING)
    date = models.DateField()
    rate = models.DecimalField(max_digits = 7,decimal_places = 2)
    boxes_out = models.IntegerField()
    boxes_return = models.IntegerField()
    price = models.DecimalField(max_digits = 8,decimal_places = 2,blank=True,null=True)

    def __str__(self):
        return self.items.itemname

    @property
    def lifespan(self):
        return '%s - present' % self.date.strftime('%m/%d/%Y')

    @property
    def get_price(self):
        return self.rate * (self.boxes_out - self.boxes_return)
    
    def save(self,*args,**kwargs):
        self.price = self.get_price
        super(sale,self).save(*args,**kwargs)

    
    


