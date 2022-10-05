from django.shortcuts import render

def index(request):
    return render(request, 'archone/logo_making.html')
