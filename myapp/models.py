from django.db import models

# Create your models here.
class Assets:
    AssetName:str
    value:float

class React(models.Model):
    employee = models.CharField(max_length=30)
    department = models.CharField(max_length=200)

class Product(models.Model):
    name = models.CharField(max_length=30)
