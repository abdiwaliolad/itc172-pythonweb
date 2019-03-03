from django.test import TestCase
from .models import Meeting,Resource,MeetingMinutes

class MeetingTest(TestCase):
    def test_stringOutput(self):
        meeting=Meeting(meetingtittle='soccer team')
        self.assertEqual(str(meeting),meeting.meetingtittle)

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'Meeting')


class MeetingMinutesTest(TestCase):
    def test_stringOutput(self):
        meetingminutes=MeetingMinutes(minutetext='50 minutes')
        self.assertEqual(str(meetingminutes),MeetingMinutes.minutetext)

    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'MeetingMinutes')


class ResourceTest(TestCase):
    def test_stringOutput(self):
        resource=Resource(resourcename='soccer field')
        self.assertEqual(str(resource), resource.resourcename)

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'Resource')

