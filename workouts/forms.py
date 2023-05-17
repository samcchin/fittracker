from django.forms import ModelForm
from workouts.models import Workout


class WorkoutForm(ModelForm):
    class Meta:
        model = Workout
        fields = ("title", "date", "workout_type", "notes")
