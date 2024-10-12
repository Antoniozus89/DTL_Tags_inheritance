from django.urls import path
from task4.views import main_page, price_page, cart_page, Menu

urlpatterns = [
    path('', main_page, name='main_page'),
    path('price', price_page, name='price_page'),
    path('cart', cart_page, name='cart_page'),
    path('menu/', Menu.as_view(), name='menu')
]
