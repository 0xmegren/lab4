from django.shortcuts import render
from django.http import HttpResponse


def default_view(request):
    return HttpResponse('<html><body>This is a site to calculate tax.</body></html>')

def calculate_tax(request, price):
    tax_rate = 0.15
    total = price + (price * tax_rate)
    return HttpResponse(f'<html><body>Total price including tax: {total}</body></html>')

def tax_rate_view(request):
    tax_rate = 15  
    context = {'tax_rate': tax_rate}
    return render(request, 'tax_rate.html', context)


# Create your views here.
