from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Meeting,Resource
from .form import resourceForm,MeetingForm

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def getmeeting(request):
    meeting_list= Meeting.objects.all()
    return render(request, 'club/meeting.html', {'meeting_list': meeting_list})

def resources(request):
    resource_list= Resource.objects.all()
    return render(request,'club/resources.html',{'resource_list': resource_list})

def meetingDetail(request, id):
    meeting= get_object_or_404(Meeting, pk=id) 
    return render(request, 'club/meetingdetail.html',{'meeting' : meeting})   

def newResource(request):
    form=resourceForm

    if request.method=='POST':
        form=resourceForm(request.POST)
        if form.is_valid():
            
            post=form.save(commit=True)
            post.save()
            form=resourceForm()
    else:
        form=resourceForm()
    return render(request, 'club/newResource.html', {'form': form})

def newMeeting(request):
    form=MeetingForm

    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()
    else:
        form=MeetingForm()
    return render(request, 'club/newMeeting.html', {'form': form})