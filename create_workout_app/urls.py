from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.ExerciseList.as_view(), name='home'),
    path('<int:pk>/', views.ExerciseDetail.as_view(), name='exercise_detail'),
    path('create/', views.CreateExercise.as_view(), name='create_exercise'),
]