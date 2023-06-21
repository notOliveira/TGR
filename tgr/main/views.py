from django.shortcuts import render
from django.views.generic import ListView
from .models import Game, Quote
# from .forms import GameForm
# from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    randomQuote = Quote.objects.order_by('?').first()
    
    context = {
        "randomQuote": randomQuote,
        "gameTitle": randomQuote.game.title,
        "gameWiki": randomQuote.game.wiki,
    }    
    return render(request, 'main/home.html', context)

class jogosListView(ListView):
    model = Game
    template_name = 'main/jogos.html'
    context_object_name = 'jogos'
    ordering = ['title']
