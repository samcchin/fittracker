from django.shortcuts import render, get_object_or_404, redirect
from workouts.models import Workout
from workouts.forms import WorkoutForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def list_workouts(request):
    list_workouts = Workout.objects.filter(owner=request.user)
    context = {
        'list_workouts': list_workouts,
    }
    return render(request, 'workouts/list.html', context)


@login_required
def show_workout(request, id):
    workout_detail = get_object_or_404(Workout, id=id)
    context = {
        "workout_detail": workout_detail,
    }
    return render(request, "workouts/detail.html", context)


@login_required
def create_workout(request):
    if request.method == "POST":
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(False)
            workout.owner = request.user
            workout.save()
            return redirect("list_workouts")
    else:
        form = WorkoutForm()
    context = {
        "form": form,
    }
    return render(request, "workouts/create.html", context)
