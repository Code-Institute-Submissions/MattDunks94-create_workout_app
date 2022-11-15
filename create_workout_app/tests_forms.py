from django.test import TestCase
from .forms import CreateExerciseForm


class TestCreateExerciseForm(TestCase):

    def test_exercise_name_required(self):
        form = CreateExerciseForm({'exercise': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('exercise', form.errors.keys())
        self.assertEqual(form.errors['exercise'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = CreateExerciseForm()
        self.assertEqual(form.Meta.fields, ['exercise', 'sets', 'reps', 'weight', 'workout'])
