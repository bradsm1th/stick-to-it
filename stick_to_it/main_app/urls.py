from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('cards/', views.cards_index, name='index'),
  path('cards/archive', views.cards_archive, name='archive'),
  path('cards/<int:card_id>/complete', views.cards_complete, name='complete'),
  path('cards/<int:card_id>/', views.cards_detail, name='detail'),
  path('cards/create/', views.CardCreate.as_view(), name='card_create'),
  path('cards/<int:pk>/update/', views.CardUpdate.as_view(), name='card_update'),
  path('cards/<int:pk>/delete/', views.CardDelete.as_view(), name='card_delete'),
  path('accounts/signup/', views.signup, name='signup'),
]