from django.urls import path
from . import views
#added a url path here from views.py file
urlpatterns  = [
    path('about',views.about,name='about'),
    path('',views.index,name='index')
]