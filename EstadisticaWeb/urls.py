from django.urls import path
from EstadisticaWeb import views
urlpatterns = [
    path('',views.index, name="index"),
    path('Informacion',views.Informacion),
    path('Perfil',views.perfil),
    path('Login',views.login),
    path('Recover',views.recover),
    path('Prueba',views.prueba),
]
