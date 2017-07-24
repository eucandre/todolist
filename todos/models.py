from django.db import models
from datetime import datetime
# Create your models here.
class Todos(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField(default=datetime.now(),blank=True)
    def __str__(self):
        return self.title

