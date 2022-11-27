from django.test import TestCase
from .models import WorkoutCategory


class TestModels(TestCase):

    def test_featured_image_placeholder_as_default(self):
        workout = WorkoutCategory.objects.create(title='Test Workout')
        self.assertEqual(workout.featured_image, 'placeholder')