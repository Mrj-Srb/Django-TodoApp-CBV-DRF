from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path('tasks/',views.TaskListAPIView.as_view(),name='api-tasks-list'),
    path('tasks/<int:pk>/',views.TaskDetailAPIView.as_view(),name='api-tasks-detail'),

]