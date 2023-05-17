from django.urls import path
from exercises.views import create_exercise, show_my_exercises


urlpatterns = [
    path("create/", create_exercise, name="create_exercise"),
    path("mine/", show_my_exercises, name="show_my_exercises"),
]
