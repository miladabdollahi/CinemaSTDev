from django.contrib import admin

from apps.core.admin import ModelAdminBase
from apps.movie.models import MovieSchedule, Movie
from apps.room.models import Room


@admin.register(Movie)
class MovieAdmin(ModelAdminBase):
    list_display = ('title',)
    ordering = ('-created_time',)
    date_hierarchy = 'created_time'


@admin.register(MovieSchedule)
class MovieScheduleAdmin(ModelAdminBase):
    list_display = ('title', 'room_id', 'movie_id', 'start_time', 'end_time')
    ordering = ('-created_time',)
    raw_id_fields = ('room',)
    date_hierarchy = 'start_time'

    def room_id(self, obj):
        return self.get_detail_page(Room, obj.room_id)

    def movie_id(self, obj):
        return self.get_detail_page(Movie, obj.movie_id)

    @staticmethod
    def title(obj):
        return obj.movie.title
