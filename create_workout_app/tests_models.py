from django.test import TestCase
from .models import WorkoutCategory


class TestModels(TestCase):
    
    def test_featured_image_default(self):
        workout = WorkoutCategory.objects.create(title='Test Workout')
        self.assertContains(workout.featured_image.default)
