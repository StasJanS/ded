from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

# Create your views here.
from .forms import UserRegisterForm, UserLoginForm
from .models import Foto, Jear, Fakt
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

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
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрированы')
            return redirect('index')
        else:
            messages.error(request, 'Ошибка регстрации - Метелица закружила-завела!')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'ded_app/register.html', context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'ded_app/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')


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


def letter(request):
    return render(request, 'ded_app/letter.html')
