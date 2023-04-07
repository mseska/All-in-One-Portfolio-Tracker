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
    path('api/stock-price', views.get_list, name='get_list'),
    
]