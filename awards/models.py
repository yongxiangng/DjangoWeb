from django.db import models

# Create your models here.

class Award(models.Model):
    date = models.IntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True, default='')
    
    def __str__(self):
        return self.title

    def year(self):
        return self.date.year
    
    def month(self):
        return self.date.strftime('%b')
