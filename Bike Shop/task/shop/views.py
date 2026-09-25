from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views import generic

from .models import Bike, Order


class BikeListView(generic.ListView):
    model = Bike
    template_name = 'shop/bikes.html'
    context_object_name = 'bikes'

from django.views import generic

from .models import Bike, Basket
from .forms import OrderForm


class BikeDetailView(generic.DetailView):
    model = Bike
    template_name = "shop/bike.html"
    context_object_name = "bike"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        bike = self.object

        frame_available = bike.frame.quantity >= 1
        seat_available = bike.seat.quantity >= 1
        tires_available = bike.tire.quantity >= 2

        if bike.has_basket:
            basket_available = Basket.objects.filter(
                quantity__gte=1
            ).exists()
        else:
            basket_available = True

        available = (
            frame_available
            and seat_available
            and tires_available
            and basket_available
        )

        context["available"] = available

        if available:
            context["form"] = OrderForm()

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        bike = self.object

        form = OrderForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)

            order.bike = bike
            order.status = "P"

            order.save()

            bike.frame.quantity -= 1
            bike.frame.save()

            bike.seat.quantity -= 1
            bike.seat.save()

            bike.tire.quantity -= 2
            bike.tire.save()

            if bike.has_basket:
                basket = Basket.objects.filter(quantity__gte=1).first()

                basket.quantity -= 1
                basket.save()

            return redirect("order", pk=order.pk)

class OrderDetailView(generic.DetailView):
    model = Order
    template_name = "shop/order.html"
    context_object_name = "order"