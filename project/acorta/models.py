from django.db import models

# Create your models here.
class UrlsAcortada(models.Model):
    #esta es la url que el usuario ha introducido en el formulario
    def __str__(self):
        return self.url
    url = models.TextField(blank=False)
