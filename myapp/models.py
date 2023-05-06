from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.


class Stock2:
    symbol: str
    price : float
    change : float
    
    def to_dict(self):
        return {'symbol': self.symbol, 'price': float(self.price), 'change': self.change}


class Portfolio(models.Model):
    name = models.CharField(max_length=255)
    #id = models.CharField(max_length=255, unique=True)
    id = models.IntegerField(primary_key=True)
    data = models.JSONField(default=list)

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
