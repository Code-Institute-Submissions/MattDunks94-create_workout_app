from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class WorkoutCategory(models.Model):

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    published_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='published_by')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    featured_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title


class Exercise(models.Model):

    exercise = models.CharField(max_length=100)
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    workout = models.ForeignKey(WorkoutCategory, on_delete=models.CASCADE, related_name='workout')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['updated_on']

    def __str__(self):
        return self.exercise
        