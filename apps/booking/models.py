from django.db import models


class Booking(models.Model):
    seat = models.ForeignKey('room.Seat', on_delete=models.CASCADE)
    movie_schedule = models.ForeignKey('movie.MovieSchedule', on_delete=models.CASCADE)
    movie_start = models.DateTimeField()
    movie_end = models.DateTimeField()

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('seat', 'movie_schedule')

    def __str__(self):
        return f"Seat {self.seat} for {self.movie_schedule.movie.title}"
