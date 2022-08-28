from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.db import connection
#added a method to return http reponse using render

from .models import purchase,sale,stock
def stocks(request):
    purchase_d = reversed(purchase.objects.all())
    sale_d  = reversed(sale.objects.all())

    with connection.cursor() as cursor:
        cursor.execute("insert into stocks_stock (items_id)select id from items_item where items_item.id not in (select items_id from stocks_stock)")
        cursor.execute("update stocks_stock set box = (select sum(boxes) from stocks_purchase where stocks_stock.items_id= stocks_purchase.items_id) - (select sum(boxes_out) from stocks_sale where stocks_stock.items_id=stocks_sale.items_id) + (select sum(boxes_return) from stocks_sale where stocks_stock.items_id=stocks_sale.items_id)")
        cursor.execute("update stocks_stock set price = (select items_item.lending_price from items_item where stocks_stock.items_id = items_item.id)* box")
        
    stock_d = stock.objects.all()
    context = {
        'purchase_d': purchase_d,
        'sale_d': sale_d,
        'stock_d': stock_d,
    }

    return render(request, 'stocks/stocks.html',context)




