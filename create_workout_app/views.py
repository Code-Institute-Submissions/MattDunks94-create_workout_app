from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import WorkoutCategory, Exercise


class ExerciseList(generic.ListView):
    model = Exercise
    template_name = 'index.html'


class ExerciseDetail(generic.DetailView):
    model = Exercise
    template_name = 'exercise_detail.html'
