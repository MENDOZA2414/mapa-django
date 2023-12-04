from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from .forms import CustomUserForm

def login_user(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirigir a inicio.html si el inicio de sesión es exitoso
            return redirect(reverse('inicio:home'))
        else:
            # Usuario no válido, mostrar mensaje de error
            messages.error(request, 'Usuario o contraseña incorrectos')

    return render(request, 'users/login.html', {'error_message': error_message})

# users/views.py
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django import forms

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Iniciar sesión automáticamente después del registro
            login(request, user)

            messages.success(request, 'Registro exitoso. Bienvenido!')
            return redirect('inicio:home')  # Cambia 'inicio:home' con la URL a la que quieras redirigir al usuario después del registro
        else:
            messages.error(request, 'Error en el formulario. Por favor, corrige los campos.')
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})
