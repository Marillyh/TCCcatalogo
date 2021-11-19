from django.views.generic import TemplateView
from django.conf.urls import url
from django.contrib.auth import views as auth_views 
from . import views

urlpatterns = [
    url(r'$^', views.paginainicial),
    url(r'logar/', views.logar, name='logar'),
    url(r'logout/', views.logout_view, name='logout'),
    url(r'form-cadastro/', views.form_cadastro),
    url(r'principal/', views.paginaprincipal),
    url(r'cadastrar-usuario/', views.cadastrar_usuario, name="cadastro"),
    url(r'produto/', views.produto),
    url(r'login/', views.login),
    url(r'cadastrar-produto/', views.cadastrar_produto),
]
  