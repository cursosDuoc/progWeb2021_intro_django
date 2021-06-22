from django.core.exceptions import ValidationError
from gestorpersonas.validators import digito_verificador, patente_chilena, telefono_chileno, validar_rut
from django.test import TestCase

class ValidarRutTestCase(TestCase) :

    def test_digito_daniel(self):
        # Los tests siempre tienen 3 partes:
        # Los datos para probar:
        rut = 12656568
        dv_esperado = 2
        # La ejecución de la pruena
        dv_obtenido = digito_verificador(rut)
        # La verificación del resultado
        self.assertEqual(dv_obtenido, dv_esperado)
        # Lo mismo se podria hacer en una sola linea como: 
        # self.assertEqual(digito_verificador(12656568), 2)
        
    def test_digito_k(self):
        # Los tests siempre tienen 3 partes:
        # Los datos para probar:
        rut = 20901792
        dv_esperado = 'k'
        # La ejecución de la pruena
        dv_obtenido = digito_verificador(rut)
        # La verificación del resultado
        self.assertEqual(dv_obtenido, dv_esperado)

    def test_digito_0(self):
        # Los tests siempre tienen 3 partes:
        # Los datos para probar:
        rut = 19995161
        dv_esperado = 0
        # La ejecución de la pruena
        dv_obtenido = digito_verificador(rut)
        # La verificación del resultado
        self.assertEqual(dv_obtenido, dv_esperado)

    def test_validar_rut_negativo(self) :
        rut = "19995161-k" # este rut no es valido...
        self.assertRaises(ValidationError, validar_rut, rut)

    def test_validar_rut_positivo(self) :
        try: 
            rut = "19995161-0" 
            validar_rut(rut)
        except :
            self.fail("rut con 0, algo salio mal")
    
    def test_telefono_bueno(self) :
        telefono = '+56996236722'
        resultado = telefono_chileno(telefono)
        self.assertTrue(resultado)

    def test_telefono_parte_con_cero(self) :
        # Los casos de prueba siempre tienen la misma estructura:
        # 1 - Se juntan los datos y objetos necesarios para probar.
        telefono = '+56096236722'
        # 2 - Se efectua la prueba
        resultado = telefono_chileno(telefono)
        # 3 - Se verifica el resultado
        self.assertFalse(resultado)
        # self.assertFalse(telefono_chileno('+56096236722')) 

    def test_telefono_muy_corto(self) :
        telefono = '+569962'
        resultado = telefono_chileno(telefono)
        self.assertFalse(resultado)
    
    def test_telefono_muy_corto(self) :
        telefono = '+569962235435343'
        resultado = telefono_chileno(telefono)
        self.assertFalse(resultado)    

    def test_telefono_con_letras(self) :
        telefono = '+56llamameee'
        resultado = telefono_chileno(telefono)
        self.assertFalse(resultado)

    def test_telefono_sin_plus(self) :
        telefono = '569962585894'
        resultado = telefono_chileno(telefono)
        self.assertFalse(resultado)

    def test_telefono_con_espacios(self) :
        telefono = '+56 22 7793733'
        resultado = telefono_chileno(telefono)
        self.assertFalse(resultado)

    def test_patente_antigua(self) :
        patente = 'UN1111' 
        resultado = patente_chilena(patente)
        self.assertTrue(resultado)

    def test_patente_nueva(self) :
        patente = 'JXFG34' 
        resultado = patente_chilena(patente)
        self.assertTrue(resultado)

    def test_patente_nueva_mala(self) :
        patente = 'CACA57' # patente no valida, forma palabra. 
        resultado = patente_chilena(patente)
        self.assertFalse(resultado)