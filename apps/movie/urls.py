from rest_framework import routers

from apps.movie.api import MovieScheduleViewSet

router = routers.DefaultRouter()
router.register('movie-schedules', MovieScheduleViewSet, 'MovieSchedule')
