from django.urls import path, re_path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('',views.index,name='index'),
    path('input',views.input,name='input'),
    path('api/items/', views.add_item, name='add_item'),
    path('api/stock-price', views.get_stock_list, name='get_stock_list'),
    path('api/crypto-price', views.get_crypto_list, name='get_crypto_list'),
    path('api/myasset-price', views.get_myasset_list, name='get_currency_list'),
    path('api/commodity-price', views.get_commodity_list, name='get_commodity_list'),
    path('api/news_mainpage', views.news_api, name='news_api'),
    path('api/login/', views.login_generate_token, name='login_generate_token'),
    path('api/signUp/', views.signup_generate_token, name='signup_generate_token'),
    path('api/get-user-info-user-icon', views.get_user_info, name='get_user_info'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('api/get_portfolios/', views.get_portfolios, name='get_portfolios'),
    path('api/portfolio-data/', views.get_portfolio_data , name='get_portfolio_data'),
    path('api/create-portfolio', views.create_portfolio , name='create_portfolio'),
    path('api/all-symbols', views.all_symbols , name='all-symbols'),
    path('api/symbols-of-portfolio', views.get_symbols_of_portfolio, name='get_symbols_of_portfolio'),
    path('api/add-to-portfolio', views.add_to_portfolio, name='add_to_portfolio'),
    path('api/increase-in-portfolio', views.increase_in_portfolio, name='increase_in_portfolio'),
    path('api/decrease-in-portfolio', views.decrease_in_portfolio, name='decrease_in_portfolio'),
    path('api/get-portfolio-names', views.get_portfolio_names, name='get_portfolio_names'),
    path('api/get-asset-names', views.get_asset_names, name='get_asset_names'),
    path('api/get-weekly-data-portfolio', views.get_weekly_data_portfolio, name='get_weekly_data_portfolio'),

    
]