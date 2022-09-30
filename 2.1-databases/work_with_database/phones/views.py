from .models import Phone
from django.shortcuts import get_object_or_404, render, redirect


def index(request):
    return redirect('catalog')

def show(request):
    template = 'show.html'
    phones = Phone.objects.all()
    context = {
        'phones': phones
        }
    return render(request, template, context)


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    context = {
        'phones': phones
        }
    return render(request, template, context)


# def show_product(request, slug):
#     template = 'product.html'
#     phone = get_object_or_404(Phone, slug=slug)
#     context = {
#         'phone': phone
#         }
#     return render(request, template, context)
