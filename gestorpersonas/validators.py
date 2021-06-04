from itertools import cycle
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _ # esto es para mandar mensajes de error en otros idiomas.

# Los validadores de django mandan un ValitationError cuando 
# algo no es valido, y no hacen nada cuando algo es valido
def validar_rut(rut_completo):
    try:
        dv_ingresado = rut_completo[-1:] # el sub string desde el final -1 , hasta el final
                                         # 20901792-k -> k
        rut = rut_completo[0:-2] # el sub string desde el 0 hasta el final -2
                                        # 20901792-k -> 20901792
        dv_calculado = digito_verificador(rut)
        if (str(dv_ingresado) != str(dv_calculado)) :
            raise ValidationError(
            _("El rut ingresado no es valido - %(valor)s"), 
            params={'valor':rut_completo}
        )    
    except:
        raise ValidationError(
            _("El rut ingresado no es valido - %(valor)s"), 
            params={'valor':rut_completo}
        )



def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    digito = (-s) % 11
    if (digito == 10):
        return 'k'
    if (digito == 11): 
        return 0
    return digito


