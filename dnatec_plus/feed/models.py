from django.db import models

# Create your models here.
class Feed(models.Model):
	mensagem = models.CharField(max_length=255)
	user = models.ForeignKey('usuario.Usuario')

	def __unicode__(self):
		return self.mensagem