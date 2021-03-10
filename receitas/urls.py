from django.urls import path
from . import views

urlpatterns = [
    # 1º parâmetro é a rota, se vazio será o index
    # 2º parâmetro é a view
    # 3º parâmetro é o namespace
    path('', views.index, name='index'),
    path('<int:receita_id>', views.receita, name='receita'),
]
