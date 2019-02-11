from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    location=models.CharField(max_length=255)
    agend=models.TextField()

    def __str__(self):
        return self.meetingtitle
    
    class Meta:
        db_table='Meeting'
    
class MeetingMinutes(models.Model):
    meeting_id=models.ForeignKey(Meeting, on_delete=models.CASCADE)
    minutetext=models.TextField()
    attendance=models.ManyToManyField(User)

    def __str__(self):
        return str(self.meeting_id)
    
    class Meta:
        db_table='MeetingMinutes'


class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourceURL=models.URLField()
    resource=models.ForeignKey(Meeting, on_delete=models.CASCADE)
    enterydate=models.DateTimeField()
    resourcetype=models.ManyToManyField(User)

    def __str__(self):
        return self.resourcename

    class Meta:
        db_table='Resource'