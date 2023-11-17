import random

from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse
from .models import Planet, Category


# def index(request):
#     return HttpResponse('<h1>Главная страница</h1>')
# from .. import Planets
# from .. import Planets


def index(request):
    planets = Planet.objects.all()
    planet_1 = random.choice(planets)
    planet_2 = random.choice(planets)
    planet_3 = random.choice(planets)
    planet_4 = random.choice(planets)
    cats = Category.objects.all()
    params = {'planet_1': planet_1, 'planet_2': planet_2, 'planet_3': planet_3, 'planet_4': planet_4, 'cats': cats}

    return render(request, 'buy_planet/main_page.html', context=params)

def about(request):
    cats = Category.objects.all()
    return render(request, 'buy_planet/about.html', {'cats': cats})

def show_planets(request):
    planets = Planet.objects.all()
    cats = Category.objects.all()
    return render(request, 'buy_planet/list.html', {'planets': planets, 'cats': cats})

def check(request):
    return render(request, 'buy_planet/common.html')

def show_planet(request, planet_id): # переменная р не имеет значения!

    planet = get_object_or_404(Planet, pk=planet_id)
    return render(request, 'buy_planet/view_planet.html', {'title': planet.name, 'planet': planet})

def buy_object(request, planet_id):
    planet = get_object_or_404(Planet, pk=planet_id)
    cats = Category.objects.all()
    return render(request, 'buy_planet/bought.html', {'planet': planet, 'cats': cats})

def no(request):
    return render(request, 'buy_planet/reklam.html')

def show_by_category(request, cat_id):
    catt = get_object_or_404(Category, pk=cat_id)

    arts = Planet.objects.filter(cat=catt)

    param_list = {
        'cats': Category.objects.all(),
        'catt': catt,
        'title': catt.cat,
        'cat_selected': catt.pk,
        'articles': arts
    }

    return render(request, 'buy_planet/by_cats.html', context=param_list)

