# Import libraries needed

"""
Created by Framework
This file is where you can create views for the App
Modified by: Enrique Posada
Date: 08/11/18
"""
from django import forms
from django.core import validators
from Catalogo.models import Ordenes



class OrderForm(forms.ModelForm):
    nombre =  forms.CharField(max_length=255,required=True,widget=forms.TextInput(attrs={'class' : 'form-control','id':'nombre', 'name':'nombre'}))
    correo = forms.EmailField(max_length=255, required=True,widget=forms.TextInput(attrs={'class' : 'form-control','id':'correo', 'name':'correo'}))

    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput)

    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError("BOT DETECTADO")
        return botcatcher

    class Meta:
        # model = Order
        fields = "__all__"
