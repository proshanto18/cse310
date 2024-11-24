from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='courses/',null=True, blank=True)
    CATEGORY_CHOICES = [
        ('academic', 'Academic'),
        ('career', 'Career'),

    ]
    description = models.TextField()
    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        default='academic',
    )


    def __str__(self):
        return self.name
