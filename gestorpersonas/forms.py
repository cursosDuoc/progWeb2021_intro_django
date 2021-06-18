from django import forms

from .models import Persona
from .models import TelefonoContacto

class PersonasForm(forms.ModelForm) :
    class Meta :
        model = Persona # este formulario va asociado a la clase Persona
        fields = ('nombre', 'apellido', 'correo', 'rut') # consideramos estos campos, podria omitir alguno


class TelefonoContactoForm(forms.ModelForm) :
    class Meta :
        model = TelefonoContacto # este formulario va asociado a la clase TelefonoContacto
        fields = ('telefono', 'descripcion')