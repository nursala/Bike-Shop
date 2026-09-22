from django.shortcuts import render
from .models import Bike


def bikes(request):
    bikes = Bike.objects.all()

    context = {
        "bikes": bikes
    }

    return render(request, "templates/shop/bikes.html", context)
