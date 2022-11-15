from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.ExerciseList.as_view(), name='home'),
    path('<int:pk>/', views.ExerciseDetail.as_view(), name='exercise_detail'),
    path('create_exercise/', views.CreateExercise.as_view(), name='create_exercise'),
    path('create_workout/', views.CreateWorkoutCategory.as_view(), name='create_workout'),
    path('edit_exercise/<int:pk>/', views.EditExercise.as_view(), name='edit_exercise'),
]