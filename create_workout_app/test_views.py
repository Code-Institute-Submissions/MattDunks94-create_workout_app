from django.test import TestCase
from .models import Exercise, WorkoutCategory


class TestViews(TestCase):

    def test_get_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'templates/index.html')

    def test_get_create_exercise_page(self):
        response = self.client.get('create_exercise/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'templates/create_exercise.html')

    def test_get_create_workout_page(self):
        response = self.client.get('create_workout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'templates/create_workout.html')

    def test_get_edit_exercise_page(self):
        exercise = Exercise.objects.create(exercise='test exercise', sets=2, reps=12, weight=25)
        response = self.client.get(f'edit_exercise/{exercise.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'templates/edit_exercise.html')

    def test_get_edit_workout_page(self):
        workout = WorkoutCategory.objects.create(title='Test Workout')
        response = self.client.get(f'edit_workout/{workout.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'templates/edit_workout.html')

    def test_can_create_exercise(self):
        response = self.client.post('create_exercise/', {
            'exercise': 'Test added exercise',
            'sets': '2',
            'reps': '12',
            'weight': '25'
        })
        self.assertRedirects(response, '/')

    def test_can_create_workout(self):
        response = self.client.post('create_workout/', {
            'title': 'Test added workout'
        })
        self.assertRedirects(response, '/')

    def test_can_delete_exercise(self):
        exercise = Exercise.objects.create(exercise='test exercise', sets=2, reps=12, weight=25)
        response = self.client.get(f'delete_exercise/{exercise.id}/')
        self.assertRedirects(response, '/')
        existing_exercises = Exercise.objects.filter(id=exercise.id)
        self.assertEqual(len(existing_exercises), 0)
        