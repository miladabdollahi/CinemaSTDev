from django.db.models import OuterRef, Exists
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from apps.booking.models import Booking
from apps.core.paginations import LargePagination
from apps.core.viewsets import CoreViewSet
from apps.movie.models import MovieSchedule
from apps.room.models import Room, Seat
from apps.room.serializers import (
    RoomBaseSerializer, RoomListSerializer, SeatListInputSerializer, SeatListSerializer
)


class RoomViewSet(mixins.ListModelMixin, CoreViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomBaseSerializer

    serializers = {
        "list": RoomListSerializer,
        "get_seats": SeatListInputSerializer,
    }

    pagination_classes = {
        'get_seats': LargePagination
    }

    @action(methods=['GET'], detail=True, url_path='seats')
    def get_seats(self, request, *args, **kwargs):
        input_data = self.get_serializer(data=request.query_params)
        input_data.is_valid(raise_exception=True)
        room = self.get_object()

        movie_schedule = get_object_or_404(MovieSchedule, id=input_data.validated_data.get('movie_schedule_id'))

        seats = Seat.objects.select_related('room').filter(
            room_id=room.id
        ).annotate(
            is_booked=Exists(
                Booking.objects.filter(
                    seat_id=OuterRef('pk'),
                    movie_schedule_id=movie_schedule.id,
                    movie_start=movie_schedule.start_time,
                    movie_end=movie_schedule.end_time,
                )
            )
        )

        # because seats in big rooms can be bigger than 100 or 1000 and best way in my idea having pagination.
        # One of the other reasons for using pagination according to exist subquery to annotate data from booking table

        page = self.paginate_queryset(seats)
        if page is not None:
            serializer = SeatListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = SeatListSerializer(seats, many=True)
        return Response(serializer.data)
