from stocks.models import purchase
price = purchase.objects.get(pk=5)
box = purchase.objects.get(pk=4)
rate = purchase.objects.get(pk=3)
price.price = box.boxes * price.price
price.save()

