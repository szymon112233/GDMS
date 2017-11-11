# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'mainGDMS/home.html')

@login_required(login_url='/')
def browse(request):
    return render(request, 'mainGDMS/browse.html')

@login_required(login_url='/')
def edit(request):
    return render(request, 'mainGDMS/edit.html')

