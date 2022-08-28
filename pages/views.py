from django.shortcuts import render
from django.http import HttpResponse
#added a method to return http reponse using render
from stocks.models import purchase
def about(request):
    
    return render(request, 'pages/about.html')

def index(request):
    return render(request,'pages/index.html')


