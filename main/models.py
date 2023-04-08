from django.db import models
# Create your models here.

class TODO(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    desc = models.TextField(max_length=50)
    isFav = models.BooleanField()
    iscompleted = models.BooleanField()
    
    
    def __str__(self):
        return self.name
    