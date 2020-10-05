from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'Come visit ISKCON Mumbai!'
    dest1.img = 'destination_1.jpg'
    dest1.price = 700

    dest2 = Destination()
    dest2.name = 'Mayapur'
    dest2.desc = 'Jai Gauranga'
    dest2.img = 'destination_2.jpg'
    dest2.price = 850

    dest3 = Destination()
    dest3.name = 'Juhu'
    dest3.desc = 'Hare Krishna'
    dest3.img = 'destination_3.jpg'
    dest3.price = 950

    dests = [dest1, dest2, dest3]

    return render(request, 'index.html', {'dests': dests})