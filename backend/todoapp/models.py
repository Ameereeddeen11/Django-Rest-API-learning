from django.db import models

class ToDoList(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(null=True)
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self) -> str:
        return self.title
