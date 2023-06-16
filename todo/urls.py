from django.urls import path

from todo.views import (
    TaskListView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskStatusUpdateView
)


urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path(
        "create/",
        TaskCreateView.as_view(),
        name="task-create",
    ),
    path(
        "<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update",
    ),
    path(
        "<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete",
    ),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tag-create",
    ),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update",
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete",
    ),
    path(
        "<int:pk>/update_status/",
        TaskStatusUpdateView.as_view(),
        name="update-status"
    ),
]

app_name = "todo"
