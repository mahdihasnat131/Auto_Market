from django.db import models
from django.contrib.auth.models import User
from showroom.models import Car_Detail
# Create your models here.

class Order(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    car=models.ForeignKey(Car_Detail,on_delete=models.CASCADE)
    ordertime=models.DateTimeField(auto_now_add=True)