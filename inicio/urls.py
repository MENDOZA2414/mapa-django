from django.urls import path
from .views import index, registrar_elemento, editar_elemento

app_name = 'inicio'

urlpatterns = [
    path('home/', index, name='home'),
    path('elemento/', registrar_elemento, name='registrar_elemento'),
    path('editar/', editar_elemento, name='editar_elemento'),
    
]
