from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('mostrar-produtos/', views.showProducts, name='mostrar-produtos'),
    path('mostrar-produto/<str:pk>', views.showProduct, name='mostrar-produto'),
    path('criar-produto/', views.createProduct, name='mostrar-produto'),
    path('atualizar-produto/<str:pk>', views.updateProduct, name='atualizar-produto'),
    path('excluir-produto/<str:pk>', views.excludeProduct, name='excluir-produto')
]