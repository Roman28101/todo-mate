from django import forms

from todo.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"placeholder": "year-month-day hours:minutes"})
    )

    class Meta:
        model = Task
        fields = "__all__"
