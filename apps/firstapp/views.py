# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import User, Poke
from django.db.models import Count

def index(request):
    return render(request, 'firstapp/index.html')

def pokes(request):
    if not 'userID' in request.session:
        del request.session
        return redirect('/')
    else:
        users = User.objects.all()
        pokes = Poke.objects.all()
        userpokes = Poke.objects.filter(pokecount= request.session['userID'])
        context = {
            'alias': User.objects.get(id=request.session['userID']).alias,
            'users': users,
            'pokes':pokes,
            'userpokes': userpokes,
        }
        return render(request, 'firstapp/pokehome.html', context)

def register(request):
    res = User.objects.validregister(request.POST)
    if res["status"]:
        request.session['userID'] = res['user'].id
        return redirect('/pokes')
    else:
        for error in res["errors"]:
            messages.error(request, error)
        return redirect('/')

def login(request):
    res = User.objects.validlogin(request.POST)
    if res['status']:
        request.session['userID'] = res['user'].id
        return redirect('/pokes')
    else:
        for error in res["errors"]:
            messages.error(request, error)
        return redirect('/')
def logout(request):
    request.session.pop('userID')
    return redirect('/')

def newpoke(request):
    result = Poke.objects.newpoke(request.session['userID'])

    return redirect('/pokes')
