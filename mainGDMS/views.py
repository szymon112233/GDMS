# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db.models.fields.reverse_related import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from mainGDMS.models import *
from mainGDMS.forms import *


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
                print field
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

@login_required(login_url='/')
def editTable(request, tableName = None):
    user = request.user
    if not user.is_staff:
        return render(request, 'mainGDMS/permissionDenied.html')
    else:
        if list(tableNames.objects.filter(stringName=tableName)):
            modelName = list(tableNames.objects.filter(stringName=tableName))[0].dbName
            print modelName
            queryset = 0
            exec ("queryset = " + modelName + ".objects.all()")
            print queryset
            if request.POST:
                item_form = ItemForm(request.POST)

            if item_form.is_valid():
                book = item.objects.all()
                item_form = ItemForm(request.POST, instance=book)
                item_form.save()
                #return redirect('/index/')
        else:
            return render(request, 'mainGDMS/404.html')
            #book = Book.objects.get(pk=book_id)
            #book_form = BookForm(instance=book)

            #return render_to_response('editbook.html', {'form': book_form}, context_instance=RequestContext(request))
        #else:
         #   return render(request, 'mainGDMS/404.html')

@login_required(login_url='/')
def saveTable(request, tableName=None):
    user = request.user
    if not user.is_staff:
        return render(request, 'mainGDMS/permissionDenied.html')
    else:
        return render(request, 'mainGDMS/edit.html')



def showLogout(request):
    if request.user is not None and request.user.is_authenticated:
        logout(request)
        return render(request, 'mainGDMS/logout.html')
    else:
        return render(request, 'mainGDMS/login.html')

def editbook(request,book_id):

    queryset = Book.objects.filter(book_id=book_id)
    if request.POST:
        form=BookForm(request.POST,instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=BookForm(instance=queryset)
        template = 'editbook.html'
        book = { 'form':form }
    return render_to_response(template, book , RequestContext(request))

