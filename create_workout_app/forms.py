from django import forms
from .models import WorkoutCategory, Exercise


class CreateExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['exercise', 'sets', 'reps', 'weight', 'workout']


class CreateWorkoutCategoryForm(forms.ModelForm):
    class Meta:
        model = WorkoutCategory
        fields = ['title', 'featured_image']


class EditExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['exercise', 'sets', 'reps', 'weight', 'workout']


class EditWorkoutCategoryForm(forms.ModelForm):
    class Meta:
        model = WorkoutCategory
        fields = ['title', 'featured_image']


class DeleteExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['exercise', 'sets', 'reps', 'weight', 'workout']

