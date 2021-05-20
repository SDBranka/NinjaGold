from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('game_setup', views.game_setup),
    path('game', views.game),
    path('process_money', views.process_money),
    path('win', views.win),
    path('lose', views.lose),
    path('reset', views.reset),
]

