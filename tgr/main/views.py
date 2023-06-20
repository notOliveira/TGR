from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Game, Quote, Genre, Platform

def home(request):
    randomQuote = Quote.objects.order_by('?').first()
    
    context = {
        "randomQuote": randomQuote,
        "gameTitle": randomQuote.game.title,
        "gameWiki": randomQuote.game.wiki
    }    
    return render(request, 'main/home.html', context)

class jogosListView(ListView):
    model = Game
    template_name = 'main/jogos.html'
    context_object_name = 'jogos'
    ordering = ['title']

# Usar o LoginRequiredMixin como parâmetro para não permitir realizar o CRUD sem estar logado

class jogosCreateView(LoginRequiredMixin, CreateView):
    model = Game
    template_name = 'main/jogo_form.html'
    fields = ['title', 'genre', 'platform', 'synopsis', 'players', 'connectivity', 'wiki']

class jogoUpdateView(LoginRequiredMixin, UpdateView):
    model = Game
    template_name = 'main/jogo_edit.html'
    fields = '__all__'
    success_url = ''

class jogoDeleteView(LoginRequiredMixin, DeleteView):
    model = Game
    success_url = '/jogos'
    template_name = "main/confirmar.html"