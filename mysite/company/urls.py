from django.conf.urls import url
from django.urls import path

from .views import *

app_name = 'company'

urlpatterns = [
    url(r'^$', product_list, name='product_list'),
    path('your_name/', get_name),
    url(r'^(?P<category_slug>[-\w]+)/$', product_list, name='product_list_by_category'),
    path('c/<slug>', product_list_company, name='product_list_by_company'),
    path('comp/<slug>', company_detail, name='company_detail'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', product_detail, name='product_detail'),
    path('cart/<slug>-<id>', add_cart, name='add_cart')
]