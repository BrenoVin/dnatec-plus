# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mensagem', models.CharField(max_length=255)),
                ('user', models.ForeignKey(to='usuario.Usuario')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
