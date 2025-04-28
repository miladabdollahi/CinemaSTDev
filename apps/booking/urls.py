from rest_framework import routers

from apps.booking.api import BookingViewSet

router = routers.DefaultRouter()
router.register('booking', BookingViewSet, 'Booking')
