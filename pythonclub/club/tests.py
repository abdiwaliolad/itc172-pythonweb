from django.test import TestCase
from .models import Meeting, MeetingMinutes,Recource

# Create your tests here.

class MeetingTest(TestCase):
    def test_stringOutput(self):
        meeting=Meeting(meetintittle)

