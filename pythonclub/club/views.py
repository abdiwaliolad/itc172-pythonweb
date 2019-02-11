from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from.models import Meeting

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

#def getmeeting(request):
    #meeting_list=Meeting.objects.all()
    #return render(request, 'club/meeting.html', {'meeting_list': meeting_list} )

