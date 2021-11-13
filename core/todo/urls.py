from django.urls import path
from . import views

app_name = 'todo_app'

urlpatterns = [
    path('', views.Tasks.as_view(), name='all_tasks'),
    path('create_task/', views.CreateTask.as_view(), name='create_task'),
    path('edit_or_delite_task/<int:id>/',
         views.Task.as_view(), name='single_task')
]
