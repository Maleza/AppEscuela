
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Alumno
from .forms import AlumnoForm
from django.shortcuts import render

def home(request):
    return render(request, 'gestion/home.html')

class AlumnoListView(ListView):
    model = Alumno
    template_name = 'gestion/alumno_list.html'

class AlumnoCreateView(CreateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'gestion/alumno_form.html'
    success_url = reverse_lazy('alumno_list')

class AlumnoUpdateView(UpdateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'gestion/alumno_form.html'
    success_url = reverse_lazy('alumno_list')

class AlumnoDeleteView(DeleteView):
    model = Alumno
    template_name = 'gestion/alumno_confirm_delete.html'
    success_url = reverse_lazy('alumno_list')


