from django.urls import path, include

from . import views
from .views import jogosListView
from rest_framework.routers import DefaultRouter
from .views import GameViewSet

r = DefaultRouter()

r.register(r"games", GameViewSet, basename='games-api')

urlpatterns = [
    path('', views.home, name='home'),
    path('games/', jogosListView.as_view(), name='games'),
    path('api/', include(r.urls))
]