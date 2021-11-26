from django.shortcuts import render
from django.http import HttpResponse


post=[]

def list_posts(request):
    return render(request,'home.html',{"posts":[post]})