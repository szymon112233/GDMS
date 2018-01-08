# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.db.models.fields.reverse_related import *
from django.db.models.fields.related import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from mainGDMS.models import *
from mainGDMS.forms import *


def index(request):
    return render(request, 'mainGDMS/login.html')

@login_required(login_url='/')
def browse(request):
    return browseTable(request, 'item')

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
            if not isinstance(field, (ManyToManyRel, ManyToOneRel, OneToOneRel, ManyToManyField, )):
                print field
                collumns.append(field)

        args = {'name': tableName, 'viewName': tableName.capitalize(), 'collumns': collumns, 'data': data}
        return render(request, 'mainGDMS/browse.html', args)
    else:
        return render(request, 'mainGDMS/404.html')

@login_required(login_url='/')
def edit(request, whatToEdit = None):
    print whatToEdit
    user = request.user
    if user.is_staff:
        form = EnemiesForm()
        splitType = whatToEdit.split('_')
        print splitType
        tableName = ''
        objectID = 0
        isNew = False
        if (len(splitType) == 2):
            tableName = splitType[0]
            objectID = int(splitType[1])
        elif (len(splitType) == 1):
            tableName = splitType[0]
            isNew = True
        else:
            return render(request, 'mainGDMS/404.html')

        print tableName
        print objectID

        if (isNew):
            if request.method == "POST":
                tempTableName = tableName.capitalize()
                exec ('form = ' + tempTableName + 'Form(request.POST)')
                if form.is_valid():
                    record = form.save(commit=False)
                    record.save()
                    return redirect('/browse/' + tableName)
            else:
                tempTableName = tableName.capitalize()
                exec ('form = ' + tempTableName + 'Form()')
            return render(request, 'mainGDMS/editRecord.html', {'name': tempTableName, 'form': form})
        else:
            if list(tableNames.objects.filter(stringName=tableName)):
                modelName = list(tableNames.objects.filter(stringName=tableName))[0].dbName
                print modelName
                obj = ''
                exec ("obj = " + modelName + ".objects.get(pk=objectID)")
                #print obj
                if request.method == "POST":
                    tempTableName = tableName.capitalize()
                    exec ('form = ' + tempTableName + 'Form(request.POST, instance=obj)')
                    if form.is_valid():
                        record = form.save(commit=False)
                        record.save()
                        return redirect('/browse/' + tableName)
                else:
                    tempTableName = tableName.capitalize()
                    exec ('form = ' + tempTableName + 'Form(instance=obj)')
                    return render(request, 'mainGDMS/editRecord.html', {'name': tempTableName, 'form': form})
            else:
                return render(request, 'mainGDMS/404.html')

    else:
        return render(request, 'mainGDMS/permissionDenied.html')




@login_required(login_url='/')
def removeRecord(request, whatToRemove = None):
    user = request.user
    if not user.is_staff:
        return render(request, 'mainGDMS/permissionDenied.html')
    else:
        splitType = whatToRemove.split('_')
        if (len(splitType) == 2):
            tableName = splitType[0]
            objectID = int(splitType[1])
            if list(tableNames.objects.filter(stringName=tableName)):
                modelName = list(tableNames.objects.filter(stringName=tableName))[0].dbName
                print modelName
                obj = ''
                exec ("obj = " + modelName + ".objects.get(pk=objectID)")
                print obj
                obj.delete()
                return redirect('/browse/' + tableName)
            else:
                return render(request, 'mainGDMS/404.html')
        else:
            return render(request, 'mainGDMS/404.html')


def showLogout(request):
    if request.user is not None and request.user.is_authenticated:
        logout(request)
        return render(request, 'mainGDMS/logout.html')
    else:
        return render(request, 'mainGDMS/login.html')

