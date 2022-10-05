from django.shortcuts import render

def index(request):

    return render(request, 'archone/contact.html')

def lock(request):

    return render(request, 'archone/lock.html')

def write(request):

    return render(request, 'archone/write.html')

def message(request):

    return render(request, 'archone/message.html')