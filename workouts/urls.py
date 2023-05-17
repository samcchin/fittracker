from django.urls import path
from workouts.views import list_workouts, show_workout, create_workout


urlpatterns = [
    path("", list_workouts, name='list_workouts'),
    path("<int:id>/", show_workout, name='show_workout'),
    path("create/", create_workout, name='create_workout'),
]
