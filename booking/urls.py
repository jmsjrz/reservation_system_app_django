from django.contrib import admin
from django.urls import path, include
from booking import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Ajoutez cette ligne pour gérer la route racine
    path('login_register/', views.login_register, name='login_register'),
    path('logout/', views.logout_view, name='logout'),
    path('time_slots/', views.time_slots, name='time_slots'),
    path('book_slot/<int:slot_id>/', views.book_slot, name='book_slot'),
    path('my_reservations/', views.my_reservations, name='my_reservations'),
    path('cancel_reservation/<int:res_id>/', views.cancel_reservation, name='cancel_reservation'),
]
