from django.db import models


# Create your models here.
class Jear(models.Model):
    number = models.CharField(max_length=10, verbose_name='Год')


class Foto(models.Model):
    img = models.ImageField(verbose_name='Фото')
    jears = models.ForeignKey('Jear', on_delete=models.CASCADE, verbose_name='Год')
