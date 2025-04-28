from rest_framework import serializers

from apps.room.models import Room, Seat


class RoomBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class RoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'name',)


class SeatBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'


class SeatListSerializer(serializers.ModelSerializer):
    is_booked = serializers.SerializerMethodField()
    room_info = serializers.SerializerMethodField()

    class Meta:
        model = Seat
        fields = ('id', 'room_info', 'chair_code', 'is_booked')

    @staticmethod
    def get_is_booked(obj):
        return obj.is_booked

    @staticmethod
    def get_room_info(obj):
        return dict(
            id=obj.room_id,
            name=obj.room.name,
        )


class SeatListInputSerializer(serializers.Serializer):
    movie_schedule_id = serializers.IntegerField(min_value=1)
