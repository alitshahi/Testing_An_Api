from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=1000)
    age=models.IntegerField()
    description=models.TextField()
    date=models.DateTimeField(auto_now=True)
    
    
def __str__(self):
    return self.name
    
    
