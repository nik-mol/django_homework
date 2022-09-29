from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from pagination.settings import BUS_STATION_CSV
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open(BUS_STATION_CSV, encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        bus_stations_list = []
        for row in reader:
            bus_stations_list += [{'Name': row['Name'], 'Street': row['Street'], 'District': row['District']}]         
            
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(bus_stations_list, 10)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
