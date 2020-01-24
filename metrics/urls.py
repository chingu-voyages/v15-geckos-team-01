# URLS for personal metrics page

from django.urls import path, include

from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('metrics', views.load_metrics, name='metrics'),
    path('myTrack', views.load_myTrack, name='myTrack'),
    path('addGoal', views.addGoal, name='addGoal'),
    path('deleteGoal/<goal_id>', views.deleteGoal, name="deleteGoal"),
    path('add_GoalOne', views.add_GoalOne, name="add_GoalOne"),
    path('add_GoalTwo', views.add_GoalTwo, name="add_GoalTwo"),
    path('add_GoalThree', views.add_GoalThree, name="add_GoalThree"),
    path('add_Bookmark', views.add_Bookmark, name="add_Bookmark"),
    path('delete_Bookmark/<url_id>', views.delete_Bookmark, name="delete_Bookmark"),
]