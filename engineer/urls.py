from django.urls import path
from . import views

app_name = "engineer"

urlpatterns = [
    path("tasks/", views.task_list_view, name="task_list"),
    path("api/tasks/", views.TaskList.as_view(), name="api_task_list"),
]
