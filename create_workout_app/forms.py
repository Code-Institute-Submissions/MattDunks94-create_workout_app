from django import forms
from .models import WorkoutCategory, Exercise


class CreateExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['exercise', 'sets', 'reps', 'weight', 'workout']
