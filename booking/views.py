from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import TimeSlot, Reservation

def home(request):
    return render(request, 'booking/home.html')

def login_register(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('home')
        elif 'register' in request.POST:
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login_register')
    else:
        form = AuthenticationForm()
        register_form = UserCreationForm()

    return render(request, 'booking/login_register.html', {
        'login_form': form,
        'register_form': register_form,
    })

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def time_slots(request):
    slots = TimeSlot.objects.filter(available=True)
    return render(request, 'booking/time_slots.html', {'slots': slots})

@login_required
def book_slot(request, slot_id):
    slot = TimeSlot.objects.get(id=slot_id)
    Reservation.objects.create(user=request.user, time_slot=slot)
    slot.available = False
    slot.save()
    return redirect('time_slots')

@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'booking/my_reservations.html', {'reservations': reservations})

@login_required
def cancel_reservation(request, res_id):
    reservation = Reservation.objects.get(id=res_id)
    reservation.time_slot.available = True
    reservation.time_slot.save()
    reservation.delete()
    return redirect('my_reservations')
