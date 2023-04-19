from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class Assets:
    AssetName:str
    value:float

class React(models.Model):
    employee = models.CharField(max_length=30)
    department = models.CharField(max_length=200)

class Product(models.Model):
    name = models.CharField(max_length=30)

class Stock2:
    symbol: str
    price : float
    currency : str
    
    def to_dict(self):
        return {'symbol': self.symbol, 'price': float(self.price), 'currency': self.currency}


# class SampleUser(AbstractUser):
#        def create_user(email, password, last_login):
#         newUser = SampleUser()
#         newUser.email = email
#         newUser.password = password
#         newUser.last_login = last_login
#         return newUser

# class SampleUser(models.Model):
#     name : str
#     surname : str
#     email : str
#     password : str
#     last_login : str

#     def create_user(email, password, last_login):
#         newUser = SampleUser()
#         newUser.email = email
#         newUser.password = password
#         newUser.last_login = last_login
#         return newUser
