import factory
from django.core.files.uploadedfile import SimpleUploadedFile

from apps.movie.models import Movie, MovieSchedule
from apps.room.tests.factories import RoomFactory


class MovieFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Movie

    title = factory.Faker('sentence', nb_words=3)

    @factory.lazy_attribute
    def poster(self):
        return SimpleUploadedFile(
            name='poster.jpg',
            content=b'\x00\x01\x02',
            content_type='image/jpeg'
        )


class MovieScheduleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MovieSchedule

    room = factory.SubFactory(RoomFactory)
    movie = factory.SubFactory(MovieFactory)
    start_time = factory.Faker('date_time_this_year')
    end_time = factory.Faker('date_time_this_year')
