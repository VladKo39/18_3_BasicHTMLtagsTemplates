from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class bascet(TemplateView):
    template_name='third_task/cart.html'

class gates(TemplateView):
    template_name='third_task/games.html'

def list_main(request):
    return render(request,'third_task/platform.html')


