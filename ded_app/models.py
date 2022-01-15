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


class Fakt(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    img = models.ImageField(upload_to='image/media/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Факт'
        verbose_name_plural = 'Факты'
