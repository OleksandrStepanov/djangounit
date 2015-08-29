from django.template import RequestContext, loader
from django.shortcuts import render
from django.http import HttpResponse

def students_list(request):
    students = (
    {'id': 1,
    'first_name': u'Andriy',
    'last_name': u'Malyarchuk',
    'ticket': 220,
    'image': 'img/1.jpg'},
    {'id': 2,
    'first_name': u'Yuriy',
    'last_name': u'Chepelyuk',
    'ticket': 203,
    'image': 'img/2.jpg'},
    {'id': 3,
    'first_name': u'Sergiy',
    'last_name': u'Popov',
    'ticket': 301,
    'image': 'img/3.jpg'},)

    return render(request, 'students/students_listing.html', {'students': students} )

def students_add(request):
    return HttpResponse('<h1>Student add form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit student %s</h1>' %sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete student %s</h1>' %sid)

def groups_list(request):
    return HttpResponse('<h1>Groups listing<h1>')

def groups_add(request):
    return HttpResponse('<h1>Group add form</h1>')

def groups_edit(request, sid):
    return HttpResponse('<h1>Edit group %s</h1>' %gid)

def groups_delete(request, sid):
    return HttpResponse('<h1>Delete group %s</h1>' %gid)

def journal(request):
    return HttpResponse('<h1>journal</h1>')




# Create your views here.
