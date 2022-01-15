from django.shortcuts import render

# Create your views here.
from .models import Foto, Jear, Fakt

menu = [{'boss': 'Главная', 'url_name': 'index'},
        {'boss': 'Письмо Дедушке Морозу', 'url_name': 'letter'},
        {'boss': 'Интересные факты', 'url_name': 'fact'},
        {'boss': 'Галерея', 'url_name': 'gallery'},
        {'boss': 'Заказать на дом', 'url_name': 'order'},
        {'boss': 'Контакты', 'url_name': 'contact'},
        ]


def index(request):
    context = {'menu': menu}
    return render(request, 'ded_app/base.html', context)


def gallery(request):
    foto = Jear.objects.all()
    context = {'menu': menu, 'foto': foto}
    return render(request, 'ded_app/gallery.html', context)


def gallery_jear(request, jears):
    foto = Foto.objects.filter(jears=jears)
    z = Foto.objects.filter(id=jears)
    context = {'menu': menu, 'foto': foto, 'z': z}
    return render(request, 'ded_app/gallery_jear.html', context)


def fakt(request):
    fakt = Fakt.objects.all()
    context = {'menu': menu, 'fakt': fakt}
    return render(request, 'ded_app/fakt.html', context)
