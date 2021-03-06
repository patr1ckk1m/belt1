# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_poke'),
    ]

    operations = [
        migrations.CreateModel(
            name='PokeManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='poke',
            name='user',
        ),
        migrations.AddField(
            model_name='poke',
            name='counter',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='poke',
            name='pokers',
            field=models.ManyToManyField(related_name='poker', to='firstapp.User'),
        ),
    ]
