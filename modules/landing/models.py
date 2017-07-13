from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def user_directory_path(instance,filename):
    #Va subir la imagene en el media root de cada usuario
    return 'user_{0}/{1}'.format(instance.usuario.id,filename)

CATEGORIAS = (
    ("DP","Deportes"),
    ("VJ","Video Juegos"),
    ("AM","Animales"),
    ("MD","Moda"),
    ("AT","Autos"),
    ("OT","Otros"),

)

class Images(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User,
    on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha_creado = models.DateTimeField(auto_now=True)
    categorias = models.CharField(max_length=50,choices=CATEGORIAS)
    imagen = models.ImageField(upload_to=user_directory_path)

