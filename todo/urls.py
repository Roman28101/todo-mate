from django.urls import path

from todo.views import (
    TaskListView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView, toggle_change_status
)


urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
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
        "<int:pk>/toggle-assign/",
        toggle_change_status,
        name="toggle_change_status",
    ),
]

app_name = "todo"
