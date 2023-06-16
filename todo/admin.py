from django.contrib import admin

from todo.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("content",)
    list_filter = ("task_status", "date")


admin.site.register(Tag)
