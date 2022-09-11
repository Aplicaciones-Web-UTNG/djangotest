from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from .forms import PersonsaForm
from .models import Persona

class PersonaList(ListView):
    model = Persona
    template_name = '../personas/index.html'

    def get_queryset(self):
        return self.model.objects.all()[:2]
