from django.shortcuts import render
from django.db import connection

# Create your views here.
from .models import Amount_Received,Amount_Lended,Amount_Status

def accounts(request):
    lended_d = reversed(Amount_Lended.objects.all())
    received_d = reversed(Amount_Received.objects.all())

    with connection.cursor() as cursor:
        cursor.execute("insert into accounts_amount_status (store_name_id) select id from accounts_customer where accounts_customer.id not in (select store_name_id from accounts_amount_status) ")
        cursor.execute("update accounts_amount_status set amount = (select sum(amount_lended) from accounts_amount_lended where accounts_amount_lended.store_name_id = accounts_amount_status.store_name_id)- (select sum(amount_received) from accounts_amount_received where accounts_amount_received.store_name_id = accounts_amount_status.store_name_id)")

    amount_d = reversed(Amount_Status.objects.all())
    context = {
        'lended_d': lended_d,
        'received_d': received_d,
        'amount_d': amount_d
    }
    return render(request, 'accounts/accounts.html',context)