from rest_framework import serializers

from apps.booking.models import Booking


class BookingBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class BookingCreateSerializer(serializers.Serializer):
    seat_ids = serializers.ListField()
    movie_schedule_id = serializers.IntegerField()
