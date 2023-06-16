from django.test import TestCase

from todo.models import Tag, Task


class ModelsTest(TestCase):
    def test_task_model_str(self):
        tags = (Tag.objects.create(name="coding"), Tag.objects.create(name="work"))
        task = Task.objects.create(
            content="More coding",
        )
        task.tags.set(tags)
        self.assertEqual(str(task), "More coding")


    def test_tag_str(self):
        tag = Tag.objects.create(
            name="sleep",
        )
        self.assertEqual(str(tag), "sleep")
