from django.shortcuts import render, redirect

# Create your views here.
from .models import Foto, Jear, Fakt
from django.contrib.auth.forms import UserCreationForm
from django.contrib import  messages

menu = [{'boss': 'Главная', 'url_name': 'index'},
        {'boss': 'Письмо Дедушке Морозу', 'url_name': 'letter'},
        {'boss': 'Интересные факты', 'url_name': 'fact'},
        {'boss': 'Галерея', 'url_name': 'gallery'},
        {'boss': 'Заказать на дом', 'url_name': 'order'},
        {'boss': 'Контакты', 'url_name': 'contact'},
        ]


def index(request):
    context = {'menu': menu, 'boss': 'Главная'}
    return render(request, 'ded_app/base.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрированы')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регстрации - Метелица закружила-завела!')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'ded_app/register.html', context)


def login(request):
    return render(request, 'ded_app/login.html')


def gallery(request):
    foto = Jear.objects.all()
    context = {'menu': menu, 'foto': foto, 'boss': 'Галерея'}
    return render(request, 'ded_app/gallery.html', context)


def gallery_jear(request, jears):
    foto = Foto.objects.filter(jears=jears)
    z = Foto.objects.filter(id=jears)
    context = {'menu': menu, 'foto': foto, 'z': z, 'boss': 'Галерея'}
    return render(request, 'ded_app/gallery_jear.html', context)


def fakt(request):
    fakt = Fakt.objects.all()
    context = {'menu': menu, 'fakt': fakt, 'boss': 'Интересные факты'}
    return render(request, 'ded_app/fakt.html', context)


def fakt_detail(request, title):
    fakt_detail = Fakt.objects.filter(title=title)
    context = {'menu': menu, 'fakt_detail': fakt_detail, 'boss': title}
    return render(request, 'ded_app/fakt_detail.html', context)
