from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Produto
from django.contrib.auth import authenticate, login as auth_login, logout 
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# Create your views here.

def paginainicial(request):
    return render(request,"paginas/inicio.html")
def login(request):
    return render(request,"paginas/login.html")
def form_cadastro(request):
    return render(request, "paginas/form-cadastro.html")
def paginacatalogo(request):
    return render(request, "paginas/produto.html")
def paginaprincipal(request):
    return render(request, "paginas/principal.html")

#modelo 

def produto(request):
    produtos = Produto.objects.all()
    return render(request,'paginas/produto.html', {'produtos': produtos})

#autenticação
@require_POST
def cadastrar_usuario(request):
	nome = request.POST['input-username']
	email = request.POST['input-email']
	senha = request.POST['input-password']
		
	new_user = User.objects.create(username=nome, email=email, password=senha)
	new_user.save()
	return HttpResponseRedirect('/login/')

@require_POST
def logar(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return HttpResponseRedirect('/principal/', {'user': user})
    else:
        return HttpResponseRedirect('/')
    
@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

@require_POST
def cadastrar_produto(request):
    titulo = request.POST['titulo']
    imagem = request.POST['imagem']
    descricao = request.POST['descricao']
    tamanho = request.POST['tamanho']
    preco = request.POST['preco']

    produto = Produto.objects.create(titulo=titulo, imagem=imagem, descricao=descricao, preco=preco, tamanho=tamanho)
    produto.save()
    return HttpResponseRedirect('/principal/')
