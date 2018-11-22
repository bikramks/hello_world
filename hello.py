'''
Created on 17-Nov-2018

@author: bsahoo
'''
''' This will act as the view page in this Django project '''
from django.shortcuts import render


def welcome(request):
    return render(request,'welcome.html')