from django.urls import path
from app.controllers import users, orders, stocks

urlpatterns = [
    path('users', users.eventList, name='users'),
    path('users/<str:id>/', users.show, name='detail'),
    path('users/<str:id>/deposit', users.deposit, name='deposit'),
    path('users/<str:id>/withdraw', users.withdraw, name='withdraw'),
    path('orders/buy', orders.buy, name='buy'),
    path('orders/sell', orders.sell, name='sell'),
    path('stocks/<str:id>/', stocks.show, name='detail'),


]