from django.urls import path

from . import views
from .views import jogosListView

urlpatterns = [
    path('', views.home, name='home'),
    path('jogos/', jogosListView.as_view(), name='jogos'),
]