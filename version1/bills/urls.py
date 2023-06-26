from django.urls import path
from . import views
#added a url path here from views.py file
urlpatterns  = [
    path('',views.bills,name='bills'),

]