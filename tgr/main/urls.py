from django.urls import path

from . import views
from .views import jogosCreateView, jogosListView, jogoUpdateView, jogoDeleteView

urlpatterns = [
    path('', views.home, name='home'),
    path('jogo/<int:pk>/deletar/', jogoDeleteView.as_view(), name='jogo-deletar'),
    path('jogos/<int:pk>/', jogoUpdateView.as_view(), name='jogo-editar'),
    path('jogos/novo/', jogosCreateView.as_view(), name='jogo-novo'),
    path('jogos/', jogosListView.as_view(), name='jogos'),
    
    path('sobre/', views.sobre, name='sobre'),
    path('cardapio/', views.cardapio, name='cardapio'),
    path('contato/', views.contato, name='contato'),
    path('eventos/', views.eventos, name='eventos'),
]