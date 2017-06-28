# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 19:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_auto_20170628_1052'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PokeManager',
        ),
        migrations.RemoveField(
            model_name='poke',
            name='pokers',
        ),
        migrations.AddField(
            model_name='poke',
            name='poked',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='poked', to='firstapp.User'),
        ),
        migrations.AddField(
            model_name='poke',
            name='poker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='poker', to='firstapp.User'),
        ),
    ]
