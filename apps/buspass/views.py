from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Bus, UserBusPass
from .forms import BookPassForm
from datetime import date

from django.conf import settings

# Create your views here.

@login_required
def home(request):
    """View for home page."""

    user_bus_pass = UserBusPass.objects.filter(user=request.user).first()
    
    return render(
        request, 'home.html', {'user': request.user, 'user_bus_pass': user_bus_pass}
    )

@login_required
def select_bus(request):
    """View for selecting bus."""

    buses = Bus.objects.all()

    return render(
        request, 'select_bus.html', {'buses': buses}
    )

@login_required
def book(request, pk):
    """View for booking pass of selected bus."""

    bus = Bus.objects.get(pk=pk)
    form = BookPassForm(bus=bus)

    if request.method == "POST":
        form = BookPassForm(request.POST, bus=bus)

        if form.is_valid():
            base_bus_pass_rate = settings.BASE_BUS_PASS_RATE
            distance_from_college = form.cleaned_data['boarding_point'].distance_from_college
            bus_pass_valid_days = (form.cleaned_data['expire_at'] - date.today()).days

            bus_pass_fare = round(base_bus_pass_rate*distance_from_college*bus_pass_valid_days)


            user_bus_pass = UserBusPass.objects.create(user=request.user,
                                                    bus=bus,
                                                    boarding_point=form.cleaned_data['boarding_point'],
                                                    created_at=date.today(),
                                                    expire_at=form.cleaned_data['expire_at'],
                                                    fare=bus_pass_fare,
                                                    active=False)
        
            return redirect('payment', pk=user_bus_pass.pk)

    return render(
        request, 'book.html', {'bus':bus, 'form':form}
    )


@login_required
def payment(request, pk):
    """View for payment of booking pass."""

    user_bus_pass = UserBusPass.objects.get(pk=pk)

    if request.method == "POST":
        user_bus_pass.active = True
        user_bus_pass.save()

        return redirect('payment_successful', pk=user_bus_pass.pk)

    return render(
        request, 'payment.html', {'user_bus_pass':user_bus_pass}
    )


@login_required
def payment_successful(request, pk):
    """View for showing payment success message."""

    user_bus_pass = UserBusPass.objects.get(pk=pk)

    return render(
        request, 'payment_successful.html', {'user_bus_pass':user_bus_pass}
    )


@login_required
def view_pass(request, pk):
    """View for showing bus pass."""

    user_bus_pass = UserBusPass.objects.get(pk=pk)

    return render(
        request, 'view_pass.html', {'user_bus_pass':user_bus_pass}
    )