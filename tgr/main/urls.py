from django.urls import path, include

from . import views
from .views import jogosListView
from rest_framework.routers import DefaultRouter
from .views import GameViewSet, QuoteViewSet, PlatformViewSet, GenreViewSet

r = DefaultRouter()

r.register(r"games", GameViewSet, basename='api-games')
r.register(r"quotes", QuoteViewSet, basename='api-quotes')
r.register(r"platforms", PlatformViewSet, basename='api-platforms')
r.register(r"genres", GenreViewSet, basename='api-genres')

urlpatterns = [
    path('', views.home, name='home'),
    path('games/', jogosListView.as_view(), name='games'),
    path('about/', views.about, name='about'),
    path('api/', include(r.urls)),
    path('add-game/', views.add_game, name='add-game'),
    path('403/', views.error_403, name='error-403'),
    path('admin-panel/', views.admin_panel, name='admin-panel'),
]