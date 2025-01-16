from django.db import models
from django.forms import ModelForm
from django import forms
from .models import *


class CreateSalesForm(ModelForm):
    class Meta:
        model = BasketDb
        fields = '__all__'

