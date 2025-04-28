from django.urls import reverse
from rest_framework.test import APITestCase

from apps.movie.tests.factories import MovieFactory, MovieScheduleFactory
from apps.room.tests.factories import RoomFactory


class MovieAPITestCase(APITestCase):

    def test_list_movies(self):
        movie = MovieFactory()
        movie_schedule = MovieScheduleFactory(movie=movie)

        url = reverse('v1:MovieSchedule-list')
        response = self.client.get(url, data=dict(room_id=movie_schedule.room_id), format='json')

        self.assertEqual(url, f'/api/v1/movie-schedules/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['movie_info']['title'], movie.title)
