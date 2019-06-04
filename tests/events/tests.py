from django.test import TestCase
from django.urls import reverse
from users.models import JboUser
from events.models import Event, Participant


class TestEvent(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = JboUser.objects.create(
            email='test@example.com',
            first_name='Jim',
            last_name='Beam'
        )
        cls.event = Event.objects.create(
            title='Test Event',
            description='This is a description'
        )

    def test_save(self):
        self.assertEqual(self.event.slug, 'test-event')

    def test_is_past(self):
        self.assertFalse(self.event.is_past())


class TestParticipant(TestEvent):
    def test_event_has_no_participants(self):
        self.assertEquals(self.event.participant_set.count(), 0)

    def test_add_participant_to_event(self):
        self.participant = Participant.objects.create(
            user=self.user,
            event=self.event
        )
        self.assertEquals(self.event.participant_set.count(), 1)


class EventViewTest(TestCase):
    def test_event_list(self):
        response = self.client.get('/events/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('events/event_list.html')

    def test_event_detail(self):
        response = self.client.get('/events/')