from django.db import models

# Create your models here.

class Award(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True, default='')
    
    def __str__(self):
        return self.title
