# Generated by Django 4.2.1 on 2023-05-04 08:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("exercises", "0003_rename_leg_exercise_exercise_exercise_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exercise",
            name="weight",
            field=models.DecimalField(decimal_places=0, max_digits=5),
        ),
    ]
