from django.urls import path
from .views import home, AlumnoListView, AlumnoCreateView, AlumnoUpdateView, AlumnoDeleteView

urlpatterns = [
    path('', home, name='home'),  # Vista raíz
    path('alumnos/', AlumnoListView.as_view(), name='alumno_list'),
    path('alumnos/crear/', AlumnoCreateView.as_view(), name='alumno_create'),
    path('alumnos/editar/<int:pk>/', AlumnoUpdateView.as_view(), name='alumno_edit'),
    path('alumnos/eliminar/<int:pk>/', AlumnoDeleteView.as_view(), name='alumno_delete'),
]
