from django.urls import path
from .views import (
    TaskListView, TaskCreateView, TaskUpdateView, 
    TaskDeleteView, toggle_task_status
)

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('<int:pk>/toggle/', toggle_task_status, name='task_toggle'),
]
