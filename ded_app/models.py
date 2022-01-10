from django.db import models


# Create your models here.
class Jear(models.Model):
    number = models.CharField(max_length=10, verbose_name='Год')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Год'
        verbose_name_plural = 'Года'


class Foto(models.Model):
    img = models.ImageField(upload_to='image/media/')
    jears = models.ForeignKey('Jear', on_delete=models.CASCADE, verbose_name='Год')

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
