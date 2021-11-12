from django.contrib import admin

from .models import TodoTask


class TodoTaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created', 'updated']
    list_filter = ['author', 'created']


admin.site.register(TodoTask, TodoTaskAdmin)
