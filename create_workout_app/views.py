from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import WorkoutCategory, Exercise
from .forms import CreateExerciseForm


class ExerciseList(generic.ListView):
    model = Exercise
    template_name = 'index.html'


class ExerciseDetail(generic.DetailView):
    model = Exercise
    template_name = 'exercise_detail.html'


class CreateExercise(generic.CreateView):
    model = Exercise
    form_class = CreateExerciseForm
    template_name = 'create_exercise.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


