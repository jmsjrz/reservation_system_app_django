from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignUpForm, LoginForm
from .models import TimeSlot, Reservation

def home(request):
    return render(request, 'booking/home.html')

def login_register(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            login_form = LoginForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect('home')
        elif 'register' in request.POST:
            register_form = SignUpForm(request.POST)
            if register_form.is_valid():
                user = register_form.save()
                login(request, user)
                return redirect('home')
    else:
        login_form = LoginForm()
        register_form = SignUpForm()

    return render(request, 'booking/login_register.html', {'login_form': login_form, 'register_form': register_form})

def logout_view(request):
    logout(request)
    return redirect('home')

def time_slots(request):
    slots = TimeSlot.objects.filter(available=True)
    return render(request, 'booking/time_slots.html', {'slots': slots})

def book_slot(request, slot_id):
    slot = TimeSlot.objects.get(id=slot_id)
    Reservation.objects.create(user=request.user, time_slot=slot)
    slot.available = False
    slot.save()
    return redirect('time_slots')

def my_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'booking/my_reservations.html', {'reservations': reservations})

def cancel_reservation(request, res_id):
    reservation = Reservation.objects.get(id=res_id)
    reservation.time_slot.available = True
    reservation.time_slot.save()
    reservation.delete()
    return redirect('my_reservations')
