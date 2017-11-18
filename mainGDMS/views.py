# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db.models.fields.reverse_related import *
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

    if list(tableNames.objects.filter(stringName=tableName)):
        modelName = list(tableNames.objects.filter(stringName=tableName))[0].dbName
        print modelName
        data = list()
        exec("data = list(" +modelName +".objects.all())")
        print data
        collumns = list()
        fieldsTouple = 0
        exec ("fieldsTouple = " + modelName + "._meta.get_fields()")
        for field in fieldsTouple:
            if not isinstance(field, (ManyToManyRel, ManyToOneRel, OneToOneRel)):
                collumns.append(field)
        args = {'name': tableName, 'collumns': collumns, 'data': data}
        return render(request, 'mainGDMS/browse.html', args)
    else:
        return render(request, 'mainGDMS/404.html')

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



