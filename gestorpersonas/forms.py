from django import forms

from .models import Persona

class PersonasForm(forms.ModelForm) :
    class Meta :
        model = Persona # este formulario va asociado a la clase Persona
        fields = ('nombre', 'apellido', 'correo', 'rut') # consideramos estos campos, podria omitir alguno