from django.shortcuts import render, redirect
from .models import Curso
from django.contrib import messages

# Create your views here.

#Listar los cursos
def home(request):
    cursosListados = Curso.objects.all()
    messages.success(request, '¡Cursos listados!')
    return render (request, "cursos/gestioncursos.html", {"cursos" : cursosListados})

#Registrar nuevos cursos
def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.create(
        codigo = codigo, nombre = nombre, creditos = creditos
    ) 
    messages.success(request, '¡Curso registrado!')
    return redirect('/')


def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo = codigo)
    curso.delete()

    messages.success(request, '¡Curso eliminado!')
    
    return redirect('/')


#Accion de esitar curso 
def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.get(codigo = codigo)

    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    messages.success(request, '¡Curso actualizado!')

    return redirect('/')

#Vista de Edicion de Curso
def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo = codigo)
    return render(request, "cursos/edicionCurso.html", {"curso":curso})