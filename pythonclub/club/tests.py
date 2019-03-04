from django.test import TestCase
from .models import Meeting,Resource,MeetingMinutes

class MeetingTest(TestCase):
    def test_stringOutput(self):
        meeting=Meeting(meetingtittle='soccer team')
        self.assertEqual(str(meeting),meeting.meetingtittle)

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'Meeting')


class ResourceTest(TestCase):
    def test_stringOutput(self):
        resource=Resource(resourcename='soccer field')
        self.assertEqual(str(resource), resource.resourcename)

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'Resource')

 # Valid Form Data
    def test_MeetingForm_is_valid(self):
        form = MeetingForm(data={'meetingtittle': "soccer field", 'meetingdate': "02/22/2019", 'location': "seattle central", 'agenda': "practing soccer,shoting"})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_UserForm_invalid(self):
        form = MeetingForm(data={'meetingtittle': "soccer field", 'meetingdate': "02/22/2019", 'location': "seattle central", 'agenda': "practing soccer,shoting"})
        self.assertFalse(form.is_valid())