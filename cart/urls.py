from django.urls import path,re_path
from . import views

app_name='cart'

urlpatterns=[
    re_path(r'^$',views.CartDetail,name='CartDetail'),
    re_path(r'add/(?P<product_id>\d+)/$',views.CartAdd,name='CartAdd'),
    re_path(r'remove/(?P<product_id>\d+)/$',views.CartRemove,name='CartRemove'),
]
