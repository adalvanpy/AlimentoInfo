from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('info/', views.informacoes, name='informacoes'),
    path('deletar/<int:pk>/', views.deletar_alimento, name='deletar_alimento'),
    path('encontrados/', views.encontrados, name='encontrados'),
    path('carboidratos/', views.carboidratos, name='carboidratos'),
    path('gorduras/', views.gorduras, name='gorduras'),
    path('proteinas/', views.proteinas, name='proteinas'),
    path('cadastrar_alimento/', views.cadastrar_alimento, name='cadastrar_alimento'),
]