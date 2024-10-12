from django.urls import path
from task3.views import main_page, price_page, cart_page

urlpatterns = [
    path('', main_page ),
    path('price', price_page),
    path('cart', cart_page),

]