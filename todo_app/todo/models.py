from django.db import models

class ToDo(models.Model):
    task = models.CharField(max_length=200) # task
    completed = models.BooleanField(default=False) # is task complete?

    def check_complete(self):
        self.completed = not self.completed # default status
        self.save()

    def __str__(self):
        return self.task # task as string
