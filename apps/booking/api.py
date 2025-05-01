from rest_framework import mixins
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from django.db import IntegrityError
from apps.booking.models import Booking
from apps.booking.serializers import BookingBaseSerializer, BookingCreateSerializer
from apps.core.viewsets import CoreViewSet
from apps.movie.models import MovieSchedule


class BookingViewSet(mixins.CreateModelMixin, CoreViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingBaseSerializer

    serializers = {
        "create": BookingCreateSerializer,
    }

    def perform_create(self, serializer):
        movie_schedule = get_object_or_404(MovieSchedule, id=serializer.validated_data.get('movie_schedule_id'))
        try:
            booking_list = list()
            movie_schedule_id = serializer.validated_data.get('movie_schedule_id')
            for seat_id in serializer.validated_data.get('seat_ids'):
                booking_list.append(
                    Booking(
                        seat_id=seat_id,
                        movie_schedule_id=movie_schedule_id,
                        movie_start=movie_schedule.start_time,
                        movie_end=movie_schedule.end_time
                    )
                )

            Booking.objects.bulk_create(booking_list)
        except IntegrityError:
            raise ValidationError("One of send your seat already booked at this time.")
