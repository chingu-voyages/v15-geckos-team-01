# URLS for personal metrics page

from django.urls import path, include

from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('metrics', views.load_metrics, name='metrics'),
    path('addGoal', views.addGoal, name='addGoal'),
    path('deleteGoal/<goal_id>', views.deleteGoal, name="deleteGoal"),
]