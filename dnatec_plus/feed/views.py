from django.shortcuts import render,redirect

from usuario.models import Usuario
from models import Feed

def salvar(request):
	msg = request.POST['conteudo']
	#recebe nome
	n = request.session['user_auth']
	e = Usuario.objects.get(nome=n)
	
	a = Feed()
	a.mensagem = msg
	#converter esse tipo
	a.user_id = e.id
	a.save()

	return redirect('/perfil/')