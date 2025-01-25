from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class bascet(TemplateView):

    template_name='third_task/cart.html'

class gates(TemplateView):
    choice = 'Выбор'
    template_name='third_task/games.html'

def list_main(request):
    title="Главая страница"
    head1='Добро пожаловать в наше путешествие!'
    button1='Главная'
    button2='Выбрать ворота'
    button3='Ваш выбор'
    context={'title':title,
             'head1':head1,
             'button1':button1,
             'button2':button2,
             'button3':button3,
             }

    return render(request,'third_task/platform.html',context)


