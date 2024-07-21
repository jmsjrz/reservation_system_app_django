from django.urls import path
from .views import home, login_register, logout_view, time_slots, book_slot, my_reservations, cancel_reservation

urlpatterns = [
    path('', home, name='home'),
    path('login_register/', login_register, name='login_register'),
    path('logout/', logout_view, name='logout'),
    path('time_slots/', time_slots, name='time_slots'),
    path('book_slot/<int:slot_id>/', book_slot, name='book_slot'),
    path('my_reservations/', my_reservations, name='my_reservations'),
    path('cancel_reservation/<int:res_id>/', cancel_reservation, name='cancel_reservation'),
]
