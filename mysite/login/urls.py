from django.urls import path
from .views import *

app_name = 'login'
urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('cart', cart, name='cart'),
    path('logout', logout, name='logout'),
    path('update<id>', update, name='update'),
    path('delete<id>', delete, name='delete'),
    path('home', home, name='home'),
    path('checkout', checkout, name='checkout'),
    path('bill', bill, name='bill'),
    path('confirm', confirm, name='confirm'),
    path('charge', charge, name='charge'),
]
