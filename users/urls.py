from django.urls import path
from.import views
from .views import register_user

app_name = 'users'

urlpatterns = [
    path('login/', views.login_user, name='login_user'),
    path('register/', register_user, name='register_user'),
]