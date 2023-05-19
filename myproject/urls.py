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

from django.urls import path, re_path

from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/items/', add_item, name='add_item'),
    path('api/stock-price', get_stock_list, name='get_stock_list'),
    path('api/crypto-price',get_crypto_list, name='get_crypto_list'),
    path('api/myasset-price', get_myasset_list, name='get_currency_list'),
    path('api/commodity-price',get_commodity_list, name='get_commodity_list'),
    path('api/news_mainpage', news_api, name='news_api'),
    path('api/login/', login_generate_token, name='login_generate_token'),
    path('api/signUp/', signup_generate_token, name='signup_generate_token'),
    path('api/get-user-info-user-icon', get_user_info, name='get_user_info'),
    path('activate/<uidb64>/<token>', activate, name='activate'),
    path('api/get_portfolios/', get_portfolios, name='get_portfolios'),
    path('api/portfolio-data/', get_portfolio_data , name='get_portfolio_data'),
    path('api/create-portfolio', create_portfolio , name='create_portfolio'),
    path('api/all-symbols', all_symbols , name='all_symbols'),
    path('api/symbols-of-portfolio', get_symbols_of_portfolio, name='get_symbols_of_portfolio'),
    path('api/add-to-portfolio', add_to_portfolio, name='add_to_portfolio'),
    path('api/increase-in-portfolio', increase_in_portfolio, name='increase_in_portfolio'),
    path('api/decrease-in-portfolio', decrease_in_portfolio, name='decrease_in_portfolio'),
    path('api/get-portfolio-names', get_portfolio_names, name='get_portfolio_names'),
    path('api/get-asset-names', get_asset_names, name='get_asset_names'),
    path('api/get-weekly-data-portfolio', get_weekly_data_portfolio, name='get_weekly_data_portfolio'),
    path('api/get-weekly-data-asset', get_weekly_data_asset, name='get_weekly_data_asset'),

]
