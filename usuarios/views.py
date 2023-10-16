from django.shortcuts import get_object_or_404, redirect, render
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages

def logout(resquest):
    auth.logout(resquest)
    return redirect('login')

def login(request):
    form = LoginForms()
    if request.method == 'POST':
        form = LoginForms(request.POST)   
        if form.is_valid():
            login = form['nome_login'].value()
            senha = form['senha'].value()    

            usuario = auth.authenticate(
                request,
                username = login,
                password = senha
            )

            if usuario is not None:
                auth.login(request, usuario)
                # messages.success(request,f'Seja bem vindo! {login}', 'alert alert-success')
                return redirect('index')
            else:
                messages.error(request,'Login ou senha incorretos', 'alert alert-danger') 
                return redirect('login')

    return render(request,'usuarios/login.html',{"form":form})

def cadastro(request):
    form = CadastroForms()
    if request.method == 'POST':
        form = CadastroForms(request.POST)               
        if form.is_valid():
            if form['senha_1'].value() != form['senha_2'].value():
                messages.error(request,'As senhas não são iguais', 'alert alert-danger') 
                return redirect('cadastro')
            
            nome = form['nome_cadastro'].value()
            sobrenome = form['sobrenome_cadastro'].value()
            login = form['nome_login'].value()
            email = form['email'].value()
            senha = form['senha_1'].value()

            if User.objects.filter(username=login).exists():
                messages.error(request,'Usuario já esta cadastrado', 'alert alert-danger') 
                return redirect('cadastro')
            
            usuario = User.objects.create_user(
                username = login,
                first_name = nome,
                last_name = sobrenome,
                email = email,
                password = senha,
            )

            usuario.save()
            # messages.success(request,f'Usuário {nome}, cadastrado com sucesso!!!', 'alert alert-success')
            return redirect('login')

    return render(request,'usuarios/cadastro.html',{"form":form})