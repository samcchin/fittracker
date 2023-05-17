from django.db import models
from django.conf import settings
from workouts.models import Workout
# Create your models here.

EXERCISE_CHOICES = (
    ('Squat', 'Squat'),
    ('Deadlift', 'Deadlift'),
    ('Leg Press', 'Leg Press'),
    ('Calf Raises', 'Calf Raises'),
    ('Leg Extension', 'Leg Extension'),
    ('Lying Leg Curl', 'Lying Leg Curl'),
    ('Lat Pulldown', 'Lat Pulldown'),
    ('Bent-Over Row', 'Bent-Over Row'),
    ('Seated Cable Row', 'Seated Cable Row'),
    ('DB Shrugs', 'DB Shrugs'),
    ('Barbell Curls', 'Barbell Curls'),
    ('Reverse Curls', 'Reverse Curls'),
    ('Bench Press', 'Bench Press'),
    ('Overhead Press', 'Overhead Press'),
    ('Chest Cable Fly', 'Chest Cable Fly'),
    ('Tricep Extension', 'Tricep Extension'),
    ('Lateral Raises', 'Lateral Raises'),
)

REP_CHOICES = (
    (5, 5),
    (8, 8),
    (10, 10),
    (12, 12),
    (15, 15),
    (20, 20),
)

SET_CHOICES = (
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
)


class Exercise(models.Model):
    exercise_type = models.CharField(max_length=200, choices=EXERCISE_CHOICES)
    sets = models.PositiveIntegerField(choices=SET_CHOICES)
    reps = models.PositiveIntegerField(choices=REP_CHOICES)
    weight = models.DecimalField(max_digits=5, decimal_places=0)
    completed = models.BooleanField(default=False)
    workout = models.ForeignKey(
        Workout,
        related_name='exercises',
        on_delete=models.CASCADE,
        blank=True, null=True,
    )
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        related_name="exercises",
        on_delete=models.CASCADE
    )

    def exercise_count(self):
        return self.exercises.count()
