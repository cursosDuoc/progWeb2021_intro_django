from django import forms
from django.forms import widgets

from .models import Persona, SolicitudReserva
from .models import TelefonoContacto

class PersonasForm(forms.ModelForm) :
    class Meta :
        model = Persona # este formulario va asociado a la clase Persona
        fields = ('nombre', 'apellido', 'correo', 'rut') # consideramos estos campos, podria omitir alguno


class TelefonoContactoForm(forms.ModelForm) :
    class Meta :
        model = TelefonoContacto # este formulario va asociado a la clase TelefonoContacto
        fields = ('telefono', 'descripcion')


class SolicitudReservaForm(forms.ModelForm) :
    refugio = forms.ChoiceField(choices = (( "CI" , "Campamento Italiano"), ("RT", "Torres") ))
    class Meta:
        model = SolicitudReserva
        fields = ('noches' , 'fecha' , 'refugio')
        widgets ={
            'fecha' : forms.DateInput(attrs={'type': 'date'}),
        }