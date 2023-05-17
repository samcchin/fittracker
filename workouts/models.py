from django import forms
from django.db import models
from django.conf import settings

# Create your models here.

WORKOUTTYPE_CHOICES = (
    ('Leg', 'Leg'),
    ('Pull', 'Pull'),
    ('Push', 'Push'),
)


class Workout(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    workout_type = models.CharField(max_length=4, choices=WORKOUTTYPE_CHOICES)
    notes = models.TextField(blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="workouts",
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.title

    def exercise_count(self):
        return self.exercises.count()
