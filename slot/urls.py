from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('slot/', views.slot_game, name='slot_game'),
    path('slot/spin/', views.spin, name='spin'),
]
