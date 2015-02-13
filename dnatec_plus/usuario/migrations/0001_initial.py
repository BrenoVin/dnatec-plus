# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('email', models.CharField(unique=True, max_length=200)),
                ('senha', models.CharField(max_length=30)),
                ('amigos', models.ManyToManyField(related_name='amizades', to='usuario.Usuario')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
