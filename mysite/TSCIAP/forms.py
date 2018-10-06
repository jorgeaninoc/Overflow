from django import forms
from django.core import validators
from TSCIAP.models import Colaborador

def check_for_numeric(value):
    if value.isnumeric() == False:
        raise forms.ValidationError('Teléfono solo acepta números.')

class ColaboradorForm(forms.ModelForm):
    nombre = forms.CharField(required=True,max_length=255,widget=forms.TextInput(attrs={'class' : 'form-control','id':'nombre', 'name':'nombre'}))
    telefono=forms.CharField(required=True,max_length=255,widget=forms.TextInput(attrs={'class' : 'form-control','id':'telefono', 'name':'telefono'}),validators=[check_for_numeric])
    correo = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class' : 'form-control','id':'correo', 'name':'correo'}))
    empresa = forms.CharField(required=True,max_length=255,widget=forms.TextInput(attrs={'class' : 'form-control','id':'empresa', 'name':'empresa'}))

    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput)

    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError("BOT DETECTADO")
        return botcatcher

    class Meta:
        model = Colaborador
        fields = "__all__"
