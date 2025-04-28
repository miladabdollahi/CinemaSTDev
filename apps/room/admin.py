from django.contrib import admin

from apps.core.admin import ModelAdminBase
from apps.room.models import Seat, Room
from apps.movie.models import MovieSchedule


@admin.register(Seat)
class SeatAdmin(ModelAdminBase):
    list_display = ('room_id', 'chair_code', 'is_active')
    list_filter = ('is_active',)
    ordering = ('-created_time',)
    raw_id_fields = ('room',)

    def room_id(self, obj):
        return self.get_detail_page(Room, obj.room_id)


@admin.register(Room)
class RoomAdmin(ModelAdminBase):
    list_display = ('name', 'seats', 'movies')
    ordering = ('-created_time',)

    def seats(self, obj):
        return self.get_list_page(Seat, 'Seats of this room.', room_id=obj.id)

    def movies(self, obj):
        return self.get_list_page(MovieSchedule, 'Movies of this room.', room_id=obj.id)
