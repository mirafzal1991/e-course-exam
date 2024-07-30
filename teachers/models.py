from django.db import models

# Create your models here.

class Teacher(models.Model):
    class RatingChoices(models.TextChoices):

        Junior = 'Junior',
        Middle = 'Middle ',
        Senior = 'Senior',


    full_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    level = models.CharField(max_length=100, choices=RatingChoices.choices, default=RatingChoices.Junior.value)
    image = models.ImageField(upload_to='teachers/', null=True, blank=True)

    def __str__(self):
        return self.full_name
