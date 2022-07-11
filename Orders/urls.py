from django.urls import path
from . import views


urlpatterns = [
    path("orders/add/", views.add_order)
]