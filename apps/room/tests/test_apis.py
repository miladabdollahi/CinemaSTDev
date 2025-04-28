from django.urls import reverse
from rest_framework.test import APITestCase

from apps.movie.tests.factories import MovieFactory, MovieScheduleFactory
from apps.room.tests.factories import RoomFactory, SeatFactory


class RoomAPITestCase(APITestCase):

    def test_room_list(self):
        room = RoomFactory()

        url = reverse('v1:Room-list')
        response = self.client.get(url)

        self.assertEqual(url, f'/api/v1/rooms/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], room.id)

    def test_get_seats_of_room(self):
        room = RoomFactory()
        SeatFactory.create_batch(5, room=room)

        movie = MovieFactory()
        movie_schedule = MovieScheduleFactory(
            room=room,
            movie=movie,
            start_time="2025-04-28T10:00:00Z",
            end_time="2025-04-28T12:00:00Z",
        )

        url = reverse('v1:Room-get-seats', kwargs=dict(pk=room.id))
        response = self.client.get(url, data=dict(movie_schedule_id=movie_schedule.id), format='json')

        self.assertEqual(url, f'/api/v1/rooms/{room.id}/seats/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['room_info']['id'], room.id)

        for seat in response.data['results']:
            self.assertIn('is_booked', seat)

    def test_get_seats_invalid_movie_schedule(self):
        room = RoomFactory()
        SeatFactory.create_batch(5, room=room)

        url = reverse('v1:Room-get-seats', kwargs=dict(pk=room.id))

        # Dont send MovieSchedule
        response = self.client.get(url, data=dict(), format='json')

        self.assertEqual(response.status_code, 400)  # Must be give 400 error.
