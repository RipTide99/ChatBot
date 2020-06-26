from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'chatpage.html')

def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })