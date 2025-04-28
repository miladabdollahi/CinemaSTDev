from django.db import models


class MovieSchedule(models.Model):
    room = models.ForeignKey('room.Room', on_delete=models.CASCADE, related_name='movie_schedules')
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='movie_schedules')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_time',)

    def __str__(self):
        return f"{self.movie.title} - {self.room.name}"


class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='posters/')

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_time',)

    def __str__(self):
        return f"{self.title} ({self.start_time} - {self.end_time})"
