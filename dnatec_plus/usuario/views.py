from django.shortcuts import render,redirect
from models import Usuario
from feed.models import Feed


# Create your views here.
def index(request):
	return render(request,'index.html')

def validar(request):
	
	nome = request.POST['nome']
	senha = request.POST['senha']

	if Usuario.objects.filter(nome=nome,senha=senha).exists():
				
		request.session['nome_auth']=True
		request.session['user_auth']=nome

		return redirect('/perfil/')
	else:
		return redirect('/')


def cadastrar(request):
	try:
		novo = Usuario()
		novo.nome = request.POST['nome']
		novo.email = request.POST['email']
		novo.senha = request.POST['senha']
		novo.save()

		return redirect('/')
	except:
		return redirect('/')

def perfil(request):

	nome = request.session['user_auth']
	atual = Usuario.objects.get(nome=nome)
	mensagens = Feed.objects.filter(user_id=atual.id)	
	amigos = atual.amigos.all()
	timeline = Feed.objects.filter(user_id=amigos)

	return render(request,'perfil.html',{'nome':nome,'timeline':timeline,'mensagens':mensagens,'amigos':amigos,'request':request})

def amigo(request,a_id):
	try:
		user=Usuario.objects.get(id=a_id)
		msg=Feed.objects.filter(user_id=user.id)
		amigos=user.amigos.all()

		return render(request,'amigo.html',{'user':user,'amigos':amigos,'msg':msg,'request':request})

	except:
		return redirect('/perfil/')
def logout(request):
	del request.session['nome_auth']
	del request.session['user_auth']
	return redirect('/')

def buscar(request):
	texto = request.POST['busca']
	lista = Usuario.objects.filter(nome__startswith=texto)

	return render(request,'busca.html',{'lista':lista})

def add(request,u_id):
	try:
		a=request.session['user_auth']
		atual = Usuario.objects.get(nome=a)
		amigo=Usuario.objects.get(id=u_id)
		atual.amigos.add(amigo)
		return redirect('/perfil/')
	except:
		return redirect('/perfil/')

def rm(request,u_id):
	try:
		a=request.session['user_auth']
		atual = Usuario.objects.get(nome=a)
		amigo=Usuario.objects.get(id=u_id)
		atual.amigos.remove(amigo)
		return redirect('/perfil/')
	except:
		return redirect('/perfil/')
