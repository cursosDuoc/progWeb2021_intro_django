from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .models import Persona
from .forms import PersonasForm

# Create your views here.

def lista_personas(request):
    # return HttpResponse(Persona.objects.all())
    personas = Persona.objects.all() # recuperamos a todas las personas desde la base de datos
    return render(request, 'gestorpersonas/lista_personas.html', {'personas' : personas })


def detalles_persona(request, pk):
    persona = get_object_or_404(Persona, pk=pk) # que hace este??
    return render(request,'gestorpersonas/detalles_persona.html', {'persona':  persona} )

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
    mensaje = ""
    if 'un_rut' in request.GET.keys() :
        try :
            persona = Persona.objects.get(rut = request.GET['un_rut'] )
            return redirect('detalles_por_rut' , un_rut=request.GET['un_rut'])
            # return render(request,'gestorpersonas/detalles_persona.html', {'persona':  persona} )
        except :
            mensaje = "No se encontro el rut buscado: " + request.GET['un_rut']
    return render(request,'gestorpersonas/buscar_por_rut.html' , {'mensaje' : mensaje} )