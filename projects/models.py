from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    description = models.TextField(null=True, blank=True, default='')
    code = models.URLField()
    deployment = models.URLField()
    
    def __str__(self):
        return self.title
