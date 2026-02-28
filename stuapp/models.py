from django.db import models

# Create your models here.
class student_details(models.Model):
    name=models.CharField(max_length=100)
    emailId=models.EmailField()
    age=models.IntegerField()
    course=models.CharField(max_length=100)
    # created_at=models.DateTimeField(auto_now_add=True)
    
     