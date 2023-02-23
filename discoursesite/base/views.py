from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.


rooms = [
    {'id': 1, 'name': 'Lets learn Django'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'I love Python'}
]

def home(request):
    # return HttpResponse(('Home page' ))
    return render(request, 'index.html', {'rooms': rooms})

def room(request):
    return render(request, 'room.html')
    # return HttpResponse(('Room page' ))