from rest_framework import routers

from apps.room.api import RoomViewSet

router = routers.DefaultRouter()
router.register('rooms', RoomViewSet, 'Room')
