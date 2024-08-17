from django.urls import path
from apptask.views import task, init, tasks, projects, check_task, update_task

urlpatterns = [
    path('', init),
    path('task/', tasks),
    path('task/<int:id>', task),
    path('taskupdate/<int:id>', update_task),
    path('taskcheck/<int:id>', check_task),
    path('project/', projects)
]