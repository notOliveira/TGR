from django.urls import path, include

from . import views
from .views import GameCreateView
from rest_framework.routers import DefaultRouter
from .views import GameViewSet, QuoteViewSet, PlatformViewSet, GenreViewSet, PerspectiveViewSet, PlayersViewSet

r = DefaultRouter()

r.register(r"games", GameViewSet, basename='api-games')
r.register(r"quotes", QuoteViewSet, basename='api-quotes')
r.register(r"platforms", PlatformViewSet, basename='api-platforms')
r.register(r"genres", GenreViewSet, basename='api-genres')
r.register(r"players", PlayersViewSet, basename='api-players')
r.register(r"perspectives", PerspectiveViewSet, basename='api-perspectives')

urlpatterns = [
    # Views
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('admin-panel/', views.admin_panel, name='admin-panel'),
    path('403/', views.error_403, name='error-403'),
    path('error-403/', views.error_403_api, name='error_403_api'),
    path('get-igdb-game/<int:game_id>/', views.get_igdb_game, name='get-igdb-game'),
    
    # DefaultRouter
    path('api/v1/', include(r.urls), name='api'),
    
    # Class-based views
    path('add-game/', GameCreateView.as_view(), name='add-game'),
]