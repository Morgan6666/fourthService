from django.db import models

class Order(models.Model):
    total = models.FloatField()
    customer_name = models.CharField(max_length=100)
    customer_email = models.CharField(max_length = 100)

