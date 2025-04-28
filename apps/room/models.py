from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=50)

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# with this table we can create seats of room with celery task or admin panel or page of client in back office.
class SeatRoomConfig(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='seat_configs')
    chair_number = models.PositiveSmallIntegerField()

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)


# seats of room create with celery task or admin panel or page of client in back office.
class Seat(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='seats')
    chair_code = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('room', 'chair_code', 'is_active')
        ordering = ('-created_time',)

    def __str__(self):
        return f"Seat {self.chair_code} in {self.room.name}"
