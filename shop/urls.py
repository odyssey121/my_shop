from django.urls import path,re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name='shop'

urlpatterns = [
    re_path(r'^(?P<category_slug>[-\w]+)/$',views.ProductList,name='ProductListByCategory'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.ProductDetail,name='ProductDetail'),
    re_path(r'^$',views.ProductList,name='ProductList'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
