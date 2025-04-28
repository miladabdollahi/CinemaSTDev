import factory
from apps.booking.models import Booking


class BookingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Booking

    seat = factory.SubFactory('apps.room.tests.factories.SeatFactory')
    movie_schedule = factory.SubFactory('apps.movie.tests.factories.MovieScheduleFactory')
    movie_start = factory.LazyAttribute(lambda o: o.movie_schedule.start_time)
    movie_end = factory.LazyAttribute(lambda o: o.movie_schedule.end_time)
