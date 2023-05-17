from django.forms import ModelForm
from exercises.models import Exercise


class ExerciseForm(ModelForm):
    class Meta:
        model = Exercise
        fields = ('exercise_type', 'sets', 'reps', 'weight', 'workout','completed')
