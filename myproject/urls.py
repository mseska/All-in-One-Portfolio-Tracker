"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path 
from myapp.views import *
from myapp.views import ReactView
from django.urls import path, re_path

from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/items/', add_item, name='add_item'),
    path('api/stock-price', get_stock_list, name='get_stock_list'),
    path('api/crypto-price',get_crypto_list, name='get_crypto_list'),
    path('api/currency-price', get_currency_list, name='get_currency_list'),
    path('api/commodity-price',get_commodity_list, name='get_commodity_list'),
    #path('',include('myapp.urls')),
    #re_path(".*",TemplateView.as_view(template_name="index.html")),
    path('input', include('myapp.urls')),
    path('static', include('myapp.urls')),
    path('inputCheck', include('myapp.urls')),
    path('list', include('myapp.urls')),
    path('react', ReactView.as_view(), name='anything')

]
