from django.contrib import admin
from exercises.models import Exercise

# Register your models here.


@admin.register(Exercise)
class LegExerciseAdmin(admin.ModelAdmin):
    list_display = ("exercise_type", "sets", "reps", "weight", "completed")
