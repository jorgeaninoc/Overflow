from django import forms
from django.core import validators
from Contacto.models import Mensaje



class MensajeForm(forms.ModelForm):
    nombre =  forms.CharField(max_length=255,required=True,widget=forms.TextInput(attrs={'class' : 'form-control','id':'nombre', 'name':'nombre'}))
    correo = forms.EmailField(max_length=255, required=True,widget=forms.TextInput(attrs={'class' : 'form-control','id':'correo', 'name':'correo'}))
    mensaje = forms.CharField(max_length=255,required=True,widget=forms.Textarea(attrs={'class' : 'form-control','id':'mensaje', 'name':'mensaje','size':300}))

    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput)

    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError("BOT DETECTADO")
        return botcatcher

    class Meta:
        model = Mensaje
        fields = "__all__"
