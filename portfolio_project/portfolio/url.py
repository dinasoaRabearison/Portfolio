
from django.urls import path
from portfolio import views

app_name='portfolio'

urlpatterns = [
    path('presentation/', views.presentation),
    path('experience/', views.experience),
    path('competence/', views.competence),
    path('loisir/', views.loisir),
    path('contact/', views.contact),
    path('login/', views.login),
    path('inscription/', views.inscription),
]