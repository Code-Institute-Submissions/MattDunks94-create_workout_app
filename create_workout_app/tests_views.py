from django.test import TestCase


class TestViews(TestCase):

    def test_get_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'templates/index.html')

    def test_get_create_exercise(self):
        response = self.client.get('/create_exercise')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'templates/create_exercise.html')

    def test_get_create_workout(self):
        response = self.client.get('/create_workout')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'templates/create_workout.html')

    def test_get_exercise_detail(self):
        response = self.client.get('/<int:pk>')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'templates/exercise_detail.html')

    def test_get_edit_exercise(self):
        response = self.client.get('/edit_exercise/4')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'templates/edit_exercise.html')

    def test_get_delete_exercise(self):
        response = self.client.get('/delete_exercise/4')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'templates/delete_exercise.html')

    def test_can_create_exercise(self):
        response = self.client.post('/create_exercise')
        self.assertRedirects(response, '/')
    

