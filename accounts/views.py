from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #BIBLIOTECA DE AUTENTICAÇÃO
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def register_view(request):#FUNÇÃO DE REGISTRO
    if request.method == "POST":#SE FOR POST
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():#SE FOR VALIDO
            user_form.save()#SALVA O USUARIO
            return redirect('cars_list')
    else:
        user_form = UserCreationForm()#FORM DE USUARIO

    return render(request, 'register.html', {'user_form': user_form})#RENDERIZA A PAGINA DE REGISTRO COM O FORM

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cars_list')
        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': login_form})

def logout_view(request):
    logout(request)
    return redirect('cars_list')