from django.test import TestCase
from .forms import CreateExerciseForm


class TestExerciseForm(TestCase):

    def test_exercise_name_is_required(self):
        form = CreateExerciseForm()
        self.assertFalse(form.is_valid())
        self.assertIn('exercise', form.errors.keys())
        self.assertEqual(form.errors['exercise'][0], 'This field is required.')

    def test_fields_are_explicit_in_meta_class(self):
        form = CreateExerciseForm()
        self.assertEqual(form.Meta.fields, [
            'exercise', 'sets', 'reps', 'weight', 'workout'
            ])


