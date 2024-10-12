from django.shortcuts import render
from django.views.generic import TemplateView


def main_page(request):
    return render(request, 'fourth_task/main_page.html')


def price_page(request):
    context = {
        'games': ['Atomic Heart', 'Cyberpunk 2077', 'Cold Waters']
    }
    return render(request, 'fourth_task/price.html', context)


def cart_page(request):
    return render(request, 'fourth_task/cart_boilerplate.html')


class Menu(TemplateView):
    template_name = 'fourth_task/menu.html'
