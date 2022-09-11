from django.shortcuts import render, redirect
from .models import Persona
from .forms import PersonsaForm

# Create your views here.
def inicio(request):
    personasListar = Persona.objects.all()
    return render(request, 'personas/index.html', {'personas' : personasListar})

#Registrar nuevas personas
def crearPersona(request):
    if request.method == 'GET':
        form = PersonsaForm()
        contexto = {
            'form':form
        }
    else:
        form = PersonsaForm(request.POST)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')

    return render (request, 'personas/crear_persona.html', contexto)

def edicionPersona(request, id):
    persona = Persona.objects.get(id = id)
    if request.method == 'GET':
        form = PersonsaForm(instance = persona)
        contexto = {
            'form':form 
        }
    else:
        form = PersonsaForm(request.POST, instance = persona)
        contexto = {
            'form':form 
        }
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'personas/crear_persona.html', contexto)

def eliminarPersona(request, id):
    persona = Persona.objects.get(id = id)
    persona.delete()
    return redirect('index')