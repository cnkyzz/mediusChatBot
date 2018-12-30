# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from . import models

def index(request):
    #registering current user to database
    user = models.User()
    user.save()
    return render(request, 'chat/index.html')
