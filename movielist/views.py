from django.http import HttpResponse
from django.shortcuts import render

def intro(request):
    return render(request, 'movielist/intro.html', {})