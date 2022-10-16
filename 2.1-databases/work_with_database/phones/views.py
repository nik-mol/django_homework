from django.shortcuts import HttpResponse, get_object_or_404, redirect, render

from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'  
    sort = request.GET.get('sort', 'name')
    if sort == 'name':
       phones = Phone.objects.all().order_by('name')  
    if sort == 'min_price':
       phones = Phone.objects.all().order_by('price')  
    if sort == 'max_price':
       phones = Phone.objects.all().order_by('-price')     

    context = {
        'phones': phones
        }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)
    context = {
        'phone': phone
        }
    return render(request, template, context)


