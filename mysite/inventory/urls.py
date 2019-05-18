from django.urls import path, include
from .views import *
from django.conf.urls import url

app_name = 'inventory'
urlpatterns = [
    path('', stock, name='stock'),
    path('list', product_list, name='product_list'),
    path('cat/<category_slug>', product_list, name='product_list_by_category'),
    path('c/<slug>', product_list_company, name='product_list_by_company'),
    path('stock/<id>', add_stock, name='add_stock'),
    path('remove/<id>/<ty>', remove_stock, name='remove_stock'),
    path('update/<id>/<ty>', update_stock, name='update_stock'),
    path('delete/<id>', delete_stock, name='delete_stock'),
]