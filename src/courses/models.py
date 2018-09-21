from django.db import models
from django.urls import reverse

# Create your models here.

class Course(models.Model):
    name        = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("courses:course-detail", kwargs={"id":self.id})
