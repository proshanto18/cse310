from django.db import models

class Lecture(models.Model):

    lecture_name=models.CharField(max_length=100)
    notes= models.TextField()
    video = models.FileField(upload_to='videos/',null=True,blank=True)
    image= models.ImageField(upload_to='photos/',null=True,blank=True)

    def __str__(self) -> str:
        return self.lecture_name
