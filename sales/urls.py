from django.urls import path
from .views import *


urlpatterns = [
    path('sales', sales, name='sales'),

    path('add_product/<int:pk>', add_product, name='add_product'),
    path('remove_product/<int:pk>', remove_product, name='remove_product'),
    path('eliminate_product/<int:pk>', eliminate_product, name='eliminate_product'),
    path('clean_basket', clean_basket, name='clean_basket'),

    path('save_basket/<pk>', save_basket, name='save_basket'),
    path('close_basket', close_basket, name='close_basket'),

]

