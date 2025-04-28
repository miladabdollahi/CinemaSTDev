from rest_framework import serializers

from apps.movie.models import MovieSchedule


class MovieScheduleBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSchedule
        fields = '__all__'


class MovieScheduleListSerializer(serializers.ModelSerializer):
    movie_info = serializers.SerializerMethodField()
    room_info = serializers.SerializerMethodField()

    class Meta:
        model = MovieSchedule
        fields = ('id', 'room_info', 'movie_info')

    @staticmethod
    def get_movie_info(obj):
        return dict(
            title=obj.movie.title,
            start_time=obj.start_time,
            end_time=obj.end_time
        )

    @staticmethod
    def get_room_info(obj):
        return dict(
            id=obj.room_id,
            name=obj.room.name,
        )
