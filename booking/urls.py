from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('time_slots/', views.time_slots, name='time_slots'),
    path('book_slot/<int:slot_id>/', views.book_slot, name='book_slot'),
    path('my_reservations/', views.my_reservations, name='my_reservations'),
    path('cancel_reservation/<int:res_id>/', views.cancel_reservation, name='cancel_reservation'),
]
