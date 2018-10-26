"""
Created by Framework
This file is where the forms used in the App are declared.
Modified by: Jorge Nino
Date: 19/10/18
"""
# Import libraries used.
from django import forms
from django.core import validators
from Colabora.models import Colaborador

# Check if the column of the input is numeric.
def check_for_numeric(value):
    if value.isnumeric() == False:
        raise forms.ValidationError('Teléfono solo acepta números.')

# Declare the form for the Colabora Site
class ColaboradorForm(forms.ModelForm):
    # Declare all the inputs of the form.
    nombre = forms.CharField(required=True,max_length=255,widget=forms.TextInput(attrs={'class' : 'form-control','id':'nombre', 'name':'nombre'}))
    telefono=forms.CharField(required=True,max_length=255,widget=forms.TextInput(attrs={'class' : 'form-control','id':'telefono', 'name':'telefono'}),validators=[check_for_numeric])
    correo = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class' : 'form-control','id':'correo', 'name':'correo'}))
    empresa = forms.CharField(required=True,max_length=255,widget=forms.TextInput(attrs={'class' : 'form-control','id':'empresa', 'name':'empresa'}))
    # Declare a hidden field to catch bots.
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput)

    # Function to detect bots and clear the botcatcher
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError("BOT DETECTADO")
        return botcatcher
    # Class to change super Class attributes
    class Meta:
        # Set the mdoel to Colaborador
        model = Colaborador
        fields = "__all__"
