from django.db import models
# Create your models here.

class TODO(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    desc = models.TextField(max_length=50)
    isFav = models.BooleanField()
    
    
    
    def __str__(self):
        return self.name
    
class todoItems (models.Model):
        name = models.CharField(max_length=20, blank=True, null=True)
        desc = models.CharField(max_length=50, blank=True, null=True)
        iscompleted = models.BooleanField()
        todo = models.ForeignKey(TODO, on_delete=models.SET_NULL, null=True)
        statusChoices = (
        ('to-do','to-do'),
        ('in-progress','in-progress'),
        ('done','done'),
        )
        status = models.CharField(max_length=12,choices=statusChoices)
        

    