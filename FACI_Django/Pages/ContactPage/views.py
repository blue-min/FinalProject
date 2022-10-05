from django.shortcuts import render

def index(request):

    return render(request, 'archone/contact.html')

def lock(request):

    return render(request, 'archone/lock.html')