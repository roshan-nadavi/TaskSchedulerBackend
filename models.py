from django.db import models

class Drink(models.Model):
    task = models.CharField(max_length=100)
    dueDate = models.CharField(max_length=10)
    urgency = models.CharField(max_length=10)
    def __str__(self) -> str:
        return self.task + "  " + self.dueDate
class Completedtasks(models.Model):
    task = models.CharField(max_length=100)
    urgency = models.CharField(max_length=10)
    def __str__(self) -> str:
        return self.task + "  " + self.urgency