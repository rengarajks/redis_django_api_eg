from django.db import models

class Product_list(models.Model):
    name=models.CharField(max_length=120)
    catgory=models.CharField(max_length=12)
    price=models.IntegerField()
    