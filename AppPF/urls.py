from django.contrib import admin
from django.urls import path, include
from AppPF.views import inicio,Funciones

urlpatterns=[
    path('Inicio/', inicio),
    path('Funciones/', Funciones),
    path('AppPF/', include('AppPF.urls')),
]
