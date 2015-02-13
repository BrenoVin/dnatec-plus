# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20150211_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='amigos',
            field=models.ManyToManyField(related_name='amizades', to='usuario.Usuario', blank=True),
            preserve_default=True,
        ),
    ]
