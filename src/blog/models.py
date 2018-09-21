from django.db import models
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    topic       = models.CharField(max_length=120) #max_length = required
    text        = models.TextField(blank=True, null=True)
    author      = models.CharField(max_length=120)

    def get_absolute_url(self):
        return reverse("blog:article-detail", kwargs={"id":self.id})
