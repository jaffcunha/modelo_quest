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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('usuario_ptr', models.OneToOneField(parent_link=True, to='treinamentoOOP.Usuario', serialize=False, primary_key=True, auto_created=True)),
                ('nUSP', models.IntegerField(verbose_name='Número USP')),
            ],
            bases=('treinamentoOOP.usuario',),
        ),
    ]
