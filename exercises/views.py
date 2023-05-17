from django.shortcuts import render, redirect
from exercises.forms import ExerciseForm
from exercises.models import Exercise
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def create_exercise(request):
    if request.method == "POST":
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save()
            exercise.assignee = request.user
            exercise.save()
            return redirect("list_workouts")
    else:
        form = ExerciseForm()
    context = {
        "form": form,
    }
    return render(request, "exercises/create.html", context)


@login_required
def show_my_exercises(request):
    exercise_list = Exercise.objects.filter(assignee=request.user)
    context = {
        "exercises_lists": exercise_list,
    }
    return render(request, "exercises/detail.html", context)
