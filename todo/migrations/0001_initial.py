# Generated by Django 4.2.2 on 2023-06-15 03:23

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
            ],
            options={
                "verbose_name": "tag",
                "verbose_name_plural": "tags",
            },
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField()),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("deadline", models.DateTimeField(blank=True)),
                ("task_status", models.BooleanField(default=False)),
                ("tags", models.ManyToManyField(related_name="tasks", to="todo.tag")),
            ],
            options={
                "verbose_name": "task",
                "verbose_name_plural": "tasks",
                "ordering": ["task_status", "-date"],
            },
        ),
    ]
