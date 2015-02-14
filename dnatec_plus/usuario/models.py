from django.db import models

# Create your models here.
class Usuario(models.Model):
	nome = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	senha = models.CharField(max_length=30)
	amigos = models.ManyToManyField('Usuario', related_name='amizades',blank=True)

	def __unicode__(self):
		return self.nome