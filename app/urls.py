from django.urls import path
from .views import ColisCreateView, ColisUpdateView, colis_list, recherche_colis

urlpatterns = [
    path('colis/create/', ColisCreateView.as_view(), name='colis_create'),
    path('colis/<int:pk>/update/', ColisUpdateView.as_view(), name='colis_update'),
    path('', colis_list, name='colis_list'),
    path('recherche_colis/', recherche_colis, name='recherche_colis'),
    
]
