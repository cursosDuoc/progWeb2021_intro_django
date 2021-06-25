from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Persona, TelefonoContacto, SolicitudReserva
from .forms import PersonasForm, TelefonoContactoForm, SolicitudReservaForm, PersonasLoginForm

# Create your views here.

def lista_personas(request):
    # return HttpResponse(Persona.objects.all())
    personas = Persona.objects.all() # recuperamos a todas las personas desde la base de datos
    return render(request, 'gestorpersonas/lista_personas.html', {'personas' : personas })


def detalles_persona(request, pk):
    persona = get_object_or_404(Persona, pk=pk) # que hace este??
    telefonos = TelefonoContacto.objects.filter(persona = persona).all()
    return render(request,'gestorpersonas/detalles_persona.html', {'persona':  persona, 
    'telefonos': telefonos} )

def persona_nueva(request) :
    # necesito el formulario...
    if request.method == "POST" :
        formulario = PersonasForm(request.POST) 
        if formulario.is_valid():
            persona = formulario.save(commit=False)
            persona.save()
            return redirect('detalles_persona', pk = persona.pk)
    else :
        formulario = PersonasForm()
    return render(request,'gestorpersonas/persona_nueva.html', {'form' : formulario} )

def persona_actualizar(request, pk) :
    persona = get_object_or_404(Persona, pk=pk)
    if request.method == "POST" :
        formulario = PersonasForm(data = request.POST, instance = persona)
        if formulario.is_valid():
            formulario.save()
            return redirect('detalles_persona', pk = persona.pk)
    else :
        # Recuperamos los datos de la persona que queremos actualizar:
        formulario = PersonasForm(instance=persona)
    return render(request,'gestorpersonas/persona_actualizar.html', {'form' : formulario} )

def persona_eliminar(request, pk) :
    persona = get_object_or_404(Persona, pk=pk)
    if request.method == "POST" :
        persona.delete()
        return redirect('lista_personas')
    else :
        formulario = PersonasForm(instance=persona)
        # esto es solo para deshabilitar los campos del formulario...
        for campo in formulario.fields :
            formulario.fields[campo].disabled = True
        return render(request,'gestorpersonas/persona_eliminar.html', {'form' : formulario} )


def detalles_por_rut(request, un_rut) :
    persona = get_object_or_404(Persona, rut=un_rut) 
    return render(request,'gestorpersonas/detalles_persona.html', {'persona':  persona} )

def buscar_por_rut(request) : 
    # vamos a agregar la condicion de que es necesario estar logeado antes de buscar...
    # En Django es muy facil, porque existe un "middleware" que permite verificarlo.
    if request.user.is_authenticated :
        mensaje = ""
        if 'un_rut' in request.GET.keys() :
            try :
                persona = Persona.objects.get(rut = request.GET['un_rut'] )
                return redirect('detalles_por_rut' , un_rut=request.GET['un_rut'])
                # return render(request,'gestorpersonas/detalles_persona.html', {'persona':  persona} )
            except :
                mensaje = "No se encontro el rut buscado: " + request.GET['un_rut']
        return render(request,'gestorpersonas/buscar_por_rut.html' , {'mensaje' : mensaje} )
    else :
        return redirect('persona_login')

def persona_agregar_telefono(request, pk) :
    persona = get_object_or_404(Persona, pk=pk)
    if request.method == "POST" :
        formulario = TelefonoContactoForm(data = request.POST)
        if formulario.is_valid():
            telefonoContacto = formulario.save(commit=False)
            telefonoContacto.persona = persona
            telefonoContacto.save()
            return redirect('detalles_persona', pk = persona.pk)
    else : 
        formulario = TelefonoContactoForm()
    return render(request,'gestorpersonas/agregar_telefono.html' , 
        {'formulario' : formulario, 'persona' : persona} )

def crear_solicitud_reserva(request) :
    if request.method == "POST" :
        formulario = SolicitudReservaForm(request.POST) 
        if formulario.is_valid():
            # Aqui guardar en la BD, similar a otros casos
            return HttpResponse("Datos Validos")
    else :
        formulario = SolicitudReservaForm()
    return render(request,'gestorpersonas/crear_solicitud_reserva.html' ,{'form' : formulario})

def persona_login(request):
    if request.method == "POST" :
        formulario = PersonasLoginForm(request.POST) 
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('usuario')
            contrasena = formulario.cleaned_data.get('contrasena')
            # primero checkeamos las credenciales...
            user = authenticate(username = usuario, password = contrasena)
            if user is not None :
                # el usuario existe y la contraseña es valida: 
                login(request, user)
                return redirect('buscar_por_rut')   # lo mandamos a la pagina que require de login.
            return HttpResponse("Usuario / Contraseña no valida " + usuario)
    else :
        formulario = PersonasLoginForm()
    return render(request,'gestorpersonas/persona_login.html' ,{'form' : formulario})

def persona_logout(request) :
    logout(request)
    return redirect('persona_login')