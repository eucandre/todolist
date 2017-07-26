from django.db import models
from datetime import datetime
# Create your models here.
class Priority(models.Model):
    class Meta:
        verbose_name_plural='Priorities'
    name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Todos(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField(default=datetime.now(),blank=True)
    priority=models.ForeignKey(Priority)
    def __str__(self):
        return self.title


