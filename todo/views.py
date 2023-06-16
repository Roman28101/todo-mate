from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo/index.html"


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")

def toggle_change_status(request, pk):
    status = Task.objects.get(id=pk)
    status.task_status = not status.task_status
    status.save()
    return HttpResponseRedirect(reverse_lazy("todo:index"))
