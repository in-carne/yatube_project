from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(request, user):
#     return HttpResponse(f'<h1> Сайт Ани Каржевой </h1> <p> Привет, {user}! Я фотограф!</p>')

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'posts/index.html'
    return render(request, template)


def group_posts(request, any_slug):
    return HttpResponse(f'а у нас {any_slug}')

# В урл мы ждем парметр, и нужно его прередать в функцию для использования
# def posts_detail(request, pk):
#     return HttpResponse(f'новости группы "{pk}"')
