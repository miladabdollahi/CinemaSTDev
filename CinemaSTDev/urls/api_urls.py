from django.urls import include, path

from apps.room.urls import router as room_router
from apps.booking.urls import router as booking_router
from apps.movie.urls import router as movie_router

urlpatterns = [
    path('', include(room_router.urls)),
    path('', include(booking_router.urls)),
    path('', include(movie_router.urls)),
]
