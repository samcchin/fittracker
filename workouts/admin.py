from django.contrib import admin
from workouts.models import Workout
# Register your models here.


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "date",
        "workout_type",
        "notes",
    )
