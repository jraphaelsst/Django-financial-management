from datetime import datetime
from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import render, redirect


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        
        if not senha == confirmar_senha:
            return redirect(reverse('cadastro'))
        
        user = User.objects.filter(username=username)
        if user.exists():
            return redirect(reverse('cadastro'))
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=senha
        )
        user.save()
        
        return redirect(reverse('login'))


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
        user = auth.authenticate(username=username, password=senha)
        if not user:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha incorretos.')
            return redirect(reverse('login'))
        
        auth.login(request, user)
        return redirect('home')


def logout(request):
    auth.logout(request)
    
    messages.add_message(request, constants.INFO, 'Deslogado do sistema com sucesso.')
    return render(request, 'login.html')