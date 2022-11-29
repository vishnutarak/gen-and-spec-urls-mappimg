from django.urls import path
from app2.views import *
app_name='tarak'
urlpatterns=[
    path('a1_hai/',a1_hai,name='a1_hai'),
    path('a1_hello/',a1_hello,name='a1_hello'),
]