from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('polls', views.polls, name='polls'),
    path('<int:pk>/vote', views.vote, name='vote'),
    path('<int:pk>/results', views.results, name='results'),
    path('latest', views.latest, name='latest')
]
