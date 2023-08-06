# finance_game/views.py
from django.shortcuts import render
from .models import Game, User

def home(request):
    user = User(username='Vasdislav')
    loans = None
    return render(request, 'home.html', {'user': user, 'loans': loans})

