from . import views
from django.urls import path,re_path

app_name='payment'

urlpatterns = [
    re_path(r'^process/$',views.PaymentProcess,name='process'),
    re_path(r'^canceled/$',views.PaymentCanceled,name='canceled'),
    re_path(r'^done/$',views.PaymentDone,name='done'),
]
