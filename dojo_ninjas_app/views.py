from django.shortcuts import render, redirect
from . import models

def index(request):
    context = {
        'dojos'     : models.get_all_dojos(),
        'ninjas'    : models.get_all_ninjas()
    }

    return render(request , "index.html", context)

def table(request):
    context = {
        'dojos'     : models.get_all_dojos(),
        'ninjas'    : models.get_all_ninjas()
    }
    return render(request , "table.html" , context) 

def tree(request):

    
    context = {
        'dojos'         : models.get_all_dojos(),
        'ninjas'        : models.get_all_ninjas()
    }

    return render(request , "tree.html" , context) 

def add_dojo(request):
    models.add_dojo(request.POST)
    return redirect('/')

def delete_dojo(request, id):
    models.delete_dojo(id)
    return redirect('/table')

def add_ninja(request):
    models.add_ninja(request.POST)
    return redirect('/')

def delete_ninja(request, id):
    models.delete_ninja(id)
    return redirect('/table')