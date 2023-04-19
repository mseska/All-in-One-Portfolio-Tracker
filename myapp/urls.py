from django.urls import path, re_path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('',views.index,name='index'),
    path('input',views.input,name='input'),
    #path('inputCheck',views.inputCheck,name='inputCheck'),
    #path('static',views.static,name='static'),
    #path('list',views.list,name='list')

    #path('react',views.ReactView.as_view(),name='anything')
    path('api/items/', views.add_item, name='add_item'),
    path('api/stock-price', views.get_stock_list, name='get_stock_list'),
    path('api/crypto-price', views.get_crypto_list, name='get_crypto_list'),
    path('api/currency-price', views.get_currency_list, name='get_currency_list'),
    path('api/commodity-price', views.get_commodity_list, name='get_commodity_list'),
    path('api/news_mainpage', views.news_api, name='news_api')
]