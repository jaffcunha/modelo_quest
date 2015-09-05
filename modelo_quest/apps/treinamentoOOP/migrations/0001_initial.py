# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pesquisador',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('pesquisador_ptr', models.OneToOneField(primary_key=True, parent_link=True, serialize=False, auto_created=True, to='treinamentoOOP.Pesquisador')),
                ('nUSP', models.IntegerField(verbose_name='Número USP')),
            ],
            bases=('treinamentoOOP.pesquisador',),
        ),
    ]
