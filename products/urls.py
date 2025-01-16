from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('products', products, name='products'),
    path('createProduct', createProduct, name='createProduct'),
    path('loadCsvProducts', loadCsvProducts, name='loadCsvProducts'),
    path('editProduct/<int:pk>', editProduct, name='editProduct'),
    path('deleteProduct/<int:pk>', deleteProduct, name='deleteProduct'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
