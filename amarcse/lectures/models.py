from django.db import models
from course.models import Course

class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lectures',default=1)
    lecture_name = models.CharField(max_length=100)
    notes = models.FileField(upload_to='lectures/notes/')
    video = models.FileField(upload_to='lectures/videos/', null=True, blank=True)
    image = models.ImageField(upload_to='lectures/images/', null=True, blank=True)

    def _str_(self):
        return self.lecture_name


class Exercise(models.Model):
    lecture = models.ForeignKey(
        Lecture,
        on_delete=models.CASCADE,
        related_name='exercises'
    )
    question_file = models.FileField(
        upload_to='exercises/questions/',
        help_text="Upload a text file containing the question."
    )
    answer_file = models.FileField(
        upload_to='exercises/answers/',
        help_text="Upload a text file containing the answer code."
    )

    def _str_(self):
        return f"Exercise for {self.lecture.name} "