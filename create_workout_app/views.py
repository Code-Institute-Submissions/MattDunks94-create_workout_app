from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from .models import WorkoutCategory, Exercise
from .forms import CreateExerciseForm, CreateWorkoutCategoryForm, EditExerciseForm, EditWorkoutCategoryForm


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


class CreateWorkoutCategory(generic.CreateView):
    model = WorkoutCategory
    form_class = CreateWorkoutCategoryForm
    template_name = 'create_workout.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.published_by = self.request.user
        return super().form_valid(form)


class EditExercise(generic.UpdateView):
    model = Exercise
    form_class = EditExerciseForm
    template_name = 'edit_exercise.html'
    success_url = reverse_lazy('home')


class EditWorkoutCategory(generic.UpdateView):
    model = WorkoutCategory
    form_class = EditWorkoutCategoryForm
    template_name = 'edit_workout.html'
    success_url = reverse_lazy('home')


class DeleteExercise(generic.DeleteView):
    model = Exercise
    template_name = 'delete_exercise.html'
    success_url = reverse_lazy('home')
