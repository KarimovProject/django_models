from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import User_person
# Create your views here.
def first_names(x):
    first_names = User_person.objects.all()
    return first_names[0].first_name