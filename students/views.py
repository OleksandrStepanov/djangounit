# -*- coding: utf-8 -*-
from django.template import RequestContext, loader
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student


def students_list(request):
students = Student.objects.all()
return render(request, 'students/students_listing.html',
{'students': students})

def students_add(request):
    return HttpResponse('<h1>Student add form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit student %s</h1>' %sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete student %s</h1>' %sid)

def groups_list(request):
    groups = (
    {'id': 1,
    'group_name':u'МНП-11',
    'leader':{'id':1,'group_name': u'Попов Сергій'}},
    {'id': 2,
    'group_name':u'МНП-12',
    'leader':{'id':2, 'group_name': u'Чепелюк Юрій'}},
    {'id': 3,
    'group_name':u'МНП-13',
    'leader':{'id':3, 'group_name': u'Малярчук Андрій'}},)

    template = loader.get_template('students/students_listing_groups.html')
    context = RequestContext(request, {'groups': groups })
    return HttpResponse( template.render(context))    

#return render(request, 'students/students_listing_groups.html', {'groups': groups} )

def groups_add(request):
    return HttpResponse('<h1>Group add form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit group %s</h1>' %gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete group %s</h1>' %gid)

def journal(request):
    return HttpResponse('<h1>journal</h1>')

def journal_list(request):
    journals = (
    {'id': 1,
    'student_name':u'Попов Сергій'},
    {'id': 2,
    'student_name':u'Чепелюк Юрій'},
    {'id': 3,
    'student_name':u'Малярчук Андрій'},)
    return render(request, 'students/students_listing_visiting.html', {'journal': journals} )




# Create your views here.
