from django.db import models

# Apoderado
class Apoderado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Alumno
class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    fecha_nacimiento = models.DateField()
    apoderado = models.ForeignKey(Apoderado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

# Profesión
class Profesion(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

# Profesor
class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    profesion = models.ForeignKey(Profesion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

# Curso
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    nivel = models.CharField(max_length=50)
    profesor_jefe = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nivel} - {self.nombre}"

# Asignatura
class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

# Detalle Asignatura
class DetAsignatura(models.Model):
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    nivel_dificultad = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)

# Calificaciones
class Calificacion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=50)
    descripcion = models.TextField()
    nota = models.DecimalField(max_digits=4, decimal_places=2)

# Detalle Calificaciones
class DetCalificacion(models.Model):
    calificacion = models.ForeignKey(Calificacion, on_delete=models.CASCADE)
    comentarios = models.TextField()
    peso = models.DecimalField(max_digits=4, decimal_places=2)

# Asistencia
class Asistencia(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha = models.DateField()

# Detalle Asistencia
class DetAsistencia(models.Model):
    asistencia = models.ForeignKey(Asistencia, on_delete=models.CASCADE)
    presente = models.BooleanField()
    bitacora = models.TextField()

# Anotaciones
class Anotacion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    fecha = models.DateField()
    tipo = models.CharField(max_length=50)

# Detalle Anotaciones
class DetAnotacion(models.Model):
    anotacion = models.ForeignKey(Anotacion, on_delete=models.CASCADE)
    motivo = models.TextField()
    observaciones = models.TextField()

# Contenido de Clases
class ContenidoClase(models.Model):
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    tema = models.CharField(max_length=100)
    periodo = models.CharField(max_length=50)
    descripcion = models.TextField()

# Detalle Contenido de Clases
class DetContenidoClase(models.Model):
    contenido = models.ForeignKey(ContenidoClase, on_delete=models.CASCADE)
    objetivos = models.TextField()
    recursos = models.TextField()

# Notificaciones
class Notificacion(models.Model):
    apoderado = models.ForeignKey(Apoderado, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)
    mensaje = models.TextField()
    fecha = models.DateField()
    estado = models.CharField(max_length=20)
    remitente = models.CharField(max_length=100)
