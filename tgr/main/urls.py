from django.urls import path, include

from . import views
from .views import GameListView, GameCreateView
from rest_framework.routers import DefaultRouter
from .views import GameViewSet, QuoteViewSet, PlatformViewSet, GenreViewSet

r = DefaultRouter()

r.register(r"games", GameViewSet, basename='api-games')
r.register(r"quotes", QuoteViewSet, basename='api-quotes')
r.register(r"platforms", PlatformViewSet, basename='api-platforms')
r.register(r"genres", GenreViewSet, basename='api-genres')

urlpatterns = [
    path('', views.home, name='home'),
    path('list-games/', GameListView.as_view(), name='list-games'),
    path('add-game/', GameCreateView.as_view(), name='add-game'),
    path('about/', views.about, name='about'),
    path('api/v1/', include(r.urls), name='api'),
    path('get-igdb-game/<int:game_id>/', views.get_igdb_game, name='get-igdb-game'),
    # path('add-game/', views.add_game, name='add-game'),
    path('403/', views.error_403, name='error-403'),
    path('admin-panel/', views.admin_panel, name='admin-panel'),
    path('error-403/', views.error_403_api, name='error_403_api'),
]