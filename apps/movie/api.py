import django_filters
from rest_framework import mixins
import apps.movie.queryset as movie_queryset
from apps.core.viewsets import CoreViewSet
from apps.movie.models import MovieSchedule
from apps.movie.serializers import MovieScheduleBaseSerializer, MovieScheduleListSerializer
from apps.core.paginations import LargePagination

# I filtered movies with room, in my opinion must be handled this part of task with frontend.
class MovieScheduleViewSetFilter(django_filters.FilterSet):
    class Meta:
        model = MovieSchedule
        fields = {
            'room_id': ['exact', ],
        }


class MovieScheduleViewSet(mixins.ListModelMixin, CoreViewSet):
    queryset = MovieSchedule.objects.all()
    serializer_class = MovieScheduleBaseSerializer
    filterset_class = MovieScheduleViewSetFilter
    pagination_class = LargePagination

    serializers = {
        "list": MovieScheduleListSerializer
    }

    querysets = {
        "list": movie_queryset.get_movie_schedule_list_queryset
    }
