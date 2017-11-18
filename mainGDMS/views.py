# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from mainGDMS.models import *


def index(request):
    return render(request, 'mainGDMS/login.html')

@login_required(login_url='/')
def browse(request):
    return render(request, 'mainGDMS/browse.html')

@login_required(login_url='/')
def browseTable(request, tableName = None):
    data = list(item.objects.all())
    print item._meta.get_fields()

    args = {'name': tableName, 'collumns': '', 'data': data}
    return render(request, 'mainGDMS/browse.html', args)

@login_required(login_url='/')
def edit(request):
    user = request.user
    if user.is_staff:
        return render(request, 'mainGDMS/edit.html')
    else:
        return render(request, 'mainGDMS/permissionDenied.html')

def showLogout(request):
    if request.user is not None and request.user.is_authenticated:
        logout(request)
        return render(request, 'mainGDMS/logout.html')
    else:
        return render(request, 'mainGDMS/login.html')



