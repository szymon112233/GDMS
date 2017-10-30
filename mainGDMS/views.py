# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request, 'mainGDMS/home.html')
	
def browse(request):
    return render(request, 'mainGDMS/browse.html')
	
def edit(request):
    return render(request, 'mainGDMS/edit.html')

