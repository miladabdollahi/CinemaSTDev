from rest_framework.test import APITestCase
from django.urls import reverse
from apps.booking.models import Booking
from apps.room.tests.factories import SeatFactory
from apps.movie.tests.factories import MovieScheduleFactory
from apps.booking.tests.factories import BookingFactory


class BookingAPITestCase(APITestCase):

    def test_create_booking_successfully(self):
        seat = SeatFactory()
        movie_schedule = MovieScheduleFactory(room=seat.room)

        url = reverse('v1:Booking-list')
        response = self.client.post(
            url,
            data={
                "seat_id": seat.id,
                "movie_schedule_id": movie_schedule.id
            },
            format='json'
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Booking.objects.count(), 1)
        booking = Booking.objects.first()
        self.assertEqual(booking.seat, seat)
        self.assertEqual(booking.movie_schedule, movie_schedule)

    def test_create_booking_with_invalid_seat(self):
        seat = SeatFactory()
        movie_schedule = MovieScheduleFactory(room=seat.room)

        url = reverse('v1:Booking-list')
        response = self.client.post(
            url,
            data={
                "seat_id": 9999,  # Does not seat with this id.
                "movie_schedule_id": movie_schedule.id
            },
            format='json'
        )

        self.assertEqual(response.status_code, 400)  # Must be raised error.

    def test_create_booking_duplicate_should_fail(self):
        seat = SeatFactory()
        movie_schedule = MovieScheduleFactory(room=seat.room)

        # Make a BookingFactory
        BookingFactory(seat=seat, movie_schedule=movie_schedule)

        url = reverse('v1:Booking-list')
        response = self.client.post(
            url,
            data={
                "seat_id": seat.id,
                "movie_schedule_id": movie_schedule.id
            },
            format='json'
        )

        self.assertEqual(response.status_code, 400)  # Because we have a unique_together constraint, it should raise an error.
