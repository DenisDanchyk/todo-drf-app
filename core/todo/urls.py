from django.urls import path
from . import views

app_name = 'todo_app'

urlpatterns = [
    path('', views.Tasks.as_view(), name='all_tasks')
]