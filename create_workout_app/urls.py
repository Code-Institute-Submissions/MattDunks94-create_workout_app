from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.ExerciseList.as_view(), name='home'),
]