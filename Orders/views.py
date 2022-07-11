from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import  Response
import requests
from .models import Order
from .serializers import OrderSerializer

@api_view(http_method_names=['POST'])
def add_order(request):
    order = Order()
    order.customer_name = request.data["customer_name"]
    order.customer_email = request.data['customer_email']
    srlz = OrderSerializer(order, many= True)
    print("I'm getting customer name, and customer email")

    return Response(srlz.data)


