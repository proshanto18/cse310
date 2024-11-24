from django.db import models
from course.models import Course

class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lectures',default=1)
    lecture_name = models.CharField(max_length=100)
    notes = models.FileField(upload_to='lectures/notes/')
    video = models.FileField(upload_to='lectures/videos/', null=True, blank=True)
    image = models.ImageField(upload_to='lectures/images/', null=True, blank=True)

    def __str__(self):
        return self.lecture_name
