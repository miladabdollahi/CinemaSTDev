from apps.movie.models import MovieSchedule


def get_movie_schedule_list_queryset():
    return MovieSchedule.objects.select_related(
        'room', 'movie'
    )