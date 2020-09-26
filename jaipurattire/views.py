from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, timedelta
from clothes.models import Clothe, Size, Fabric

def home(request):
    return render(request, 'home.html')

def cart(request):
    return render(request, 'cart.html')

def newarrivals(request):
    timethreshold = datetime.now() - timedelta(hours=72)
    clothes = Clothe.objects
    return render(request, 'newarrivals.html', {'clothes':clothes})