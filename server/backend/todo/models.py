from django.db import models


class Todo(models.Model):
    body = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Todo: {self.body}, Completed: {self.completed}, Deadline: {self.deadline}"
        