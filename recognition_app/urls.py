from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    #path('recognize/', views.recognize_face, name='recognize_face'),

    path('', views.index, name='index'),
    path('recognize_faces/', views.recognize_faces, name='recognize_face'),
    path('add/', views.add_individual, name='add_individual'),
]