from audioop import reverse
from re import template
from django.template import loader # import loader
from django.shortcuts import render

import members
from .models import Members
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
#import httpResponse
from django.http import HttpResponse

#Create a def
def index(request):
    # tem = loader.get_template('myfirst.html')
    # return HttpResponse(tem.render())
    # mymembers = Members.objects.all().values()
    # output = ''
    # for x in mymembers:
    #     output += x["firstName"]
    # return HttpResponse(output)
    mymembers = Members.objects.all().values()
    tem = loader.get_template('index.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(tem.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    fname = request.POST.get('firstName')
    lname = request.POST.get('lastName')
    member = Members(firstName = fname, lastName = lname)
    member.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    member = Members.objects.get(id = id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    members = Members.objects.get(id = id)
    template = loader.get_template('update.html')
    context = {
        'members': members,
    }
    return HttpResponse(template.render(context, request))

def UpdateRecord(request, id):
    fname = request.POST.get('firstName')
    lname = request.POST.get('lastName')
    member = Members.objects.get(id = id)
    member.firstName = fname
    member.lastName = lname
    member.save()
    return HttpResponseRedirect(reverse('index'))
