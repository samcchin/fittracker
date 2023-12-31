# Generated by Django 4.2.1 on 2023-05-04 08:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("exercises", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="exercise",
            name="pull_exercise",
        ),
        migrations.RemoveField(
            model_name="exercise",
            name="push_exercise",
        ),
        migrations.AlterField(
            model_name="exercise",
            name="leg_exercise",
            field=models.CharField(
                choices=[
                    ("Squat", "Squat"),
                    ("Deadlift", "Deadlift"),
                    ("Leg Press", "Leg Press"),
                    ("Calf Raises", "Calf Raises"),
                    ("Leg Extension", "Leg Extension"),
                    ("Lying Leg Curl", "Lying Leg Curl"),
                    ("Lat Pulldown", "Lat Pulldown"),
                    ("Bent-Over Row", "Bent-Over Row"),
                    ("Seated Cable Row", "Seated Cable Row"),
                    ("DB Shrugs", "DB Shrugs"),
                    ("Barbell Curls", "Barbell Curls"),
                    ("Reverse Curls", "Reverse Curls"),
                    ("Bench Press", "Bench Press"),
                    ("Overhead Press", "Overhead Press"),
                    ("Chest Cable Fly", "Chest Cable Fly"),
                    ("Tricep Extension", "Tricep Extension"),
                    ("Lateral Raises", "Lateral Raises"),
                ],
                max_length=200,
            ),
        ),
    ]
