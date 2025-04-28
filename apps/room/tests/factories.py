import factory

from apps.room.models import Room, Seat, SeatRoomConfig


class RoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Room

    name = factory.Faker('word')


class SeatFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Seat

    room = factory.SubFactory(RoomFactory)
    chair_code = factory.Faker('random_int', min=1, max=100)
    is_active = True

