from django import forms
from django.forms import ModelForm
from mainGDMS.models import *


class ItemForm(ModelForm):

    class Meta:
        model = item

        fields = ['id', 'name', 'desc', 'type']