from django.contrib import admin

from apps.booking.models import Booking
from apps.core.admin import ModelAdminBase
from apps.room.models import Seat
from apps.movie.models import MovieSchedule


@admin.register(Booking)
class BookingAdmin(ModelAdminBase):
    list_display = ('seat_id', 'movie_schedule_id', 'movie_start', 'movie_end')
    ordering = ('-created_time',)
    raw_id_fields = ('seat', 'movie_schedule')
    date_hierarchy = 'movie_start'

    def seat_id(self, obj):
        return self.get_detail_page(Seat, obj.seat_id)

    def movie_schedule_id(self, obj):
        return self.get_detail_page(MovieSchedule, obj.movie_schedule_id)
