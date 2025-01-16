from django.db import models
from django.forms import ModelForm
from django import forms
from .models import *


class CreateProductForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
