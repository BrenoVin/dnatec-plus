from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    
    url(r'^admin/', include(admin.site.urls)),
	
	url(r'^$','usuario.views.index'),

	url(r'^validar/$','usuario.views.validar'),

	url(r'^perfil/$','usuario.views.perfil'),

	url(r'^cadastrar/$','usuario.views.cadastrar'),

	url(r'^amigo/(?P<a_id>\d+)/$','usuario.views.amigo'),

	url(r'^salvar/$','feed.views.salvar'),

	url(r'^logout/$','usuario.views.logout'),

	url(r'^buscar/$','usuario.views.buscar'),

	url(r'^add/(?P<u_id>\d+)/$','usuario.views.add'),

	url(r'^rm/(?P<u_id>\d+)/$','usuario.views.rm'),



)