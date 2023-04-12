from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Todo(models.Model):
    # gradChoices = [
    #     ('A+', '100'),
    #     ('B+', '85'),
    # ]
    # description = models.TextField()
    # grade = models.CharField(max_length=2, choices=gradChoices, null= True, blank=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE, null= True, blank=True)
    title = models.CharField(max_length=150)
    createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_description(self):
        return self.description[:30]


class TodoItem(models.Model):
    title = models.CharField(max_length=150, null= True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    isCompleted = models.BooleanField(default=False)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, null= True)

    def __str__(self):
        return self.title