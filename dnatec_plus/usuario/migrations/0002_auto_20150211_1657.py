# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='amigos',
            field=models.ManyToManyField(related_name='amizades', null=True, to='usuario.Usuario'),
            preserve_default=True,
        ),
    ]
