from django.contrib import admin
from .models import (
    Alumno,
    Apoderado,
    Profesor,
    Profesion,
    Curso,
    Asignatura,
    DetAsignatura,
    Calificacion,
    DetCalificacion,
    Asistencia,
    DetAsistencia,
    Anotacion,
    DetAnotacion,
    ContenidoClase,
    DetContenidoClase,
    Notificacion
)

# Admin Personalizados para mostrar más información útil en el panel

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'rut', 'fecha_nacimiento', 'apoderado')
    search_fields = ('nombre', 'rut')
    list_filter = ('apoderado',)

@admin.register(Apoderado)
class ApoderadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'rut', 'email', 'telefono')
    search_fields = ('nombre', 'apellido', 'rut')

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'rut', 'profesion')
    search_fields = ('nombre', 'rut')
    list_filter = ('profesion',)

@admin.register(Profesion)
class ProfesionAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion',)

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'nivel', 'profesor_jefe')
    list_filter = ('nivel',)

@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'profesor')
    search_fields = ('nombre',)
    list_filter = ('profesor',)

@admin.register(DetAsignatura)
class DetAsignaturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'asignatura', 'nivel_dificultad', 'tipo')

@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'alumno', 'asignatura', 'periodo', 'nota')
    list_filter = ('periodo', 'asignatura')
    search_fields = ('alumno__nombre',)

@admin.register(DetCalificacion)
class DetCalificacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'calificacion', 'comentarios', 'peso')

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'alumno', 'curso', 'fecha')
    list_filter = ('curso', 'fecha')

@admin.register(DetAsistencia)
class DetAsistenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'asistencia', 'presente')
    list_filter = ('presente',)

@admin.register(Anotacion)
class AnotacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'alumno', 'profesor', 'fecha', 'tipo')
    list_filter = ('tipo', 'fecha')

@admin.register(DetAnotacion)
class DetAnotacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'anotacion', 'motivo')

@admin.register(ContenidoClase)
class ContenidoClaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'asignatura', 'profesor', 'tema', 'periodo')

@admin.register(DetContenidoClase)
class DetContenidoClaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'contenido',)

@admin.register(Notificacion)
class NotificacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'alumno', 'apoderado', 'tipo', 'fecha', 'estado', 'remitente')
    list_filter = ('tipo', 'fecha', 'estado')
    search_fields = ('alumno__nombre', 'apoderado__nombre', 'remitente')
